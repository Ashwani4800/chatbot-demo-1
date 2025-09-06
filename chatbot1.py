import ollama

# Initialize the Ollama client
client = ollama.Client()

# Define the model and the input prompt
model = "llama3"  # Replace with your model name
prompt = "What is a car?"

# Send the query to the model
response = client.generate(model=model, prompt=prompt)

# Print the response from the model
print("Response from Ollama:")

print(response.response)

#This is the reponse to the specific request 
'''A car, also known as an automobile or vehicle, is a self-powered road-going motorized vehicle that is designed to transport people and goods. Here's a breakdown of what defines a car:

1. **Self-propelled**: A car has its own power source, typically an internal combustion engine (ICE) or electric motor, which powers the wheels.
2. **Road-going**: Cars are designed for use on paved roads, such as highways, streets, and parking lots.
3. **Motorized**: They have a motor that provides propulsion, allowing them to move without human power.
4. **Transportation**: Cars are primarily used to transport people (e.g., passengers) or goods (e.g., cargo).
5. **Four wheels**: Most cars have four wheels, although some may have fewer or more wheels depending on the type of vehicle.

Some common types of cars include:

1. Sedans: Passenger vehicles with a fixed roof and an enclosed rear compartment.
2. Hatchbacks: Sedans with a rear door that opens upwards to provide access to a cargo area.
3. SUVs (Sport Utility Vehicles): Tall, rugged vehicles designed for off-road use and carrying heavy loads.
4. Trucks: Open-bed vehicles used for hauling goods or equipment.
5. Electric vehicles (EVs): Cars powered solely by electric motors and batteries.

These are just a few examples of the many types of cars that exist. If you have any specific questions about cars or would like to know more about a particular type, feel free to ask!'''
