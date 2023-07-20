usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}
assistiram = []
assistiram.extend(usuarios_machine_learning)
assistiram.extend(usuarios_data_science)
print(usuarios_machine_learning)
usuarios_machine_learning.add(13)
print(usuarios_machine_learning)
usuarios_machine_learning.add(15)
print(usuarios_machine_learning)
for usuario in set(assistiram):
    print(usuario)
print(usuarios_machine_learning | usuarios_data_science)
print(usuarios_machine_learning & usuarios_data_science)
