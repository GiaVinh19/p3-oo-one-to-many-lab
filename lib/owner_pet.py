class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner = None) -> None:
        if pet_type in Pet.PET_TYPES:
            self.name = name
            self.pet_type = pet_type
            self.owner = owner
            Pet.all.append(self) # add pet instance into Pet's class variable all[]
        else:
            raise Exception("pet_type must be picked from PET_TYPES")
    
    # def to_list(self):
    #     if self.owner != None:
    #         return [self.name, self.pet_type, self.owner]
    #     return [self.name, self.pet_type]
        
    # def list_to_objects(pet_list):
    #     for sublist in pet_list:
    #         # if sublist[2]:
    #         #     return Pet.pet_method(sublist[0], sublist[1], sublist[2])
    #         sublist = Pet(sublist[0], sublist[1])
    #     return pet_list

    # def all_to_sorted_list(pet_list):
    #     string_list = []
    #     for pet_instance in pet_list:
    #         if pet_instance.owner != None:
    #             pet_instance = [pet_instance.name, pet_instance.pet_type, pet_instance.owner]
    #             string_list.append(pet_instance)
    #         else: 
    #             pet_instance = [pet_instance.name, pet_instance.pet_type]
    #             string_list.append(pet_instance)
    #     string_list.sort()
    #     pet_list = string_list
    #     return pet_list

class Owner:
    def __init__(self, name) -> None:
        self.name = name
    
    def pets(self):
        return Pet.all
    
    def add_pet(self, pet):
        if isinstance(pet, Pet): ## isinstance checks for pet instance is the same type pet instance's class
            pet.owner = self
        else:
            raise Exception("add_pet only take Pet's instance")

    def get_sorted_pets(self):
        Pet.all = sorted(Pet.all, key=lambda x: (x.name, x.pet_type, x.owner))
        return Pet.all


pet1 = Pet("Bento", "cat")
pet2 = Pet("Cookie", "dog")
pet3 = Pet("Azura", "reptile")

owner1 = Owner("Doug")

print(Pet.all) # list of instances

pet_list = Pet.all

print(Owner.get_sorted_pets("nonsensible"))

# print(Pet.all_to_sorted_list(pet_list)) # list of sorted list
# print(Pet.list_to_objects(pet_list)) # list of sorted instances