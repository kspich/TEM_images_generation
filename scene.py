import bpy
import random

# Название коллекции для наночастиц
COLLECTION_NAME = "Nanoparticles"

# Функция для очистки или создания коллекции
def setup_collection():
    # Удаляем коллекцию, если она существует
    if COLLECTION_NAME in bpy.data.collections:
        collection = bpy.data.collections[COLLECTION_NAME]
        # Удаляем все объекты в коллекции
        for obj in collection.objects:
            bpy.data.objects.remove(obj, do_unlink=True)
        # Удаляем саму коллекцию
        bpy.data.collections.remove(collection)
    
    # Создаём новую коллекцию
    collection = bpy.data.collections.new(COLLECTION_NAME)
    bpy.context.scene.collection.children.link(collection)
    return collection

# Функция для создания наночастицы
def create_nanoparticle(shape='sphere', size_nm=10, location=(0, 0, 0), collection=None):
    size = size_nm / 1000  # Конвертация нм в единицы Blender
    if shape == 'sphere':
        bpy.ops.mesh.primitive_uv_sphere_add(radius=size, location=location)
    elif shape == 'cube':
        bpy.ops.mesh.primitive_cube_add(size=size * 2, location=location)
    
    # Добавление объекта в коллекцию
    obj = bpy.context.active_object
    if collection:
        bpy.context.scene.collection.objects.unlink(obj)  # Удаляем из главной сцены
        collection.objects.link(obj)  # Добавляем в коллекцию Nanoparticles
    
    # Добавление модификатора шума для неправильной формы
    #obj = bpy.context.active_object
    #mod = obj.modifiers.new(name='Displace', type='DISPLACE')
    #texture = bpy.data.textures.new('NoiseTex', type='STUCCI')
    #mod.texture = texture
    #mod.strength = random.uniform(0.01, 0.05)  # Случайная деформация

# Создание коллекции
nanoparticle_collection = setup_collection()

# Создание нескольких наночастиц
for _ in range(10):
    shape = random.choice(['sphere', 'cube'])
    size = random.uniform(3, 5)  # Размер в нм
    x, y, z = random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1), size/1000/2
    create_nanoparticle(shape, size, (x, y, z), nanoparticle_collection)