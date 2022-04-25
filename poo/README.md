# ABSTRACT CLASSES
* can't be instantiated, the just offer an interfaz 4 the inherited subclasses 
* u can implement the methods, this way inherited subclasses don't neet to implement some code

### Clase abstracta: 
no puede ser instanciada

### Metodo abstracto: 
es un met. que no contiene implementacion

### Example
    
Este archivo contiene 5 clases  
* SerVivo (abstrac)   
* Animal  (abstrac)   
* Planta   
* AnimalHervivoro   
* AnimalCarnivoro  

la abstraccion, como su nombre lo indica sirven para **abstraer caracteristicas** de los objetos, estas clases se encargan
de **poseer** los **metodos compartidos** para **luego ser implementados** por clases que serán instacciadas. 
su objetivo es ahorar lineas de código en la compilación, por el ejemplo, si las clases A.Hervivoro y A.Carnivoro no implementaran el método abstraido y en ves de eso cada uno lo creara esto crearia una duplicacion de codigo. 

             SerVivo (abs)
            /            \
           /              \
       Planta             Animal (abs)
                           /       \
                          /         \
             AnimalCarnivoro       AnimalHervivoro


# ENCAPSULATION
The encapsulation doesn't exist in python but u can simulate it
by adding 2 underscores to the methods or attributes names

### Example   

    class person():

        __banck_account_number = "123456789"

        def __get_back_account_number(self):
            print("123456789")

u can't access the account number neither by the attribute 
not the method due to the underscore that makes it private

    



