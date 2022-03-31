voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

voting_data.insert(1, {'county': 'El Paso', 'registered_voters':461149})

arapahoe_info = voting_data[0]
voting_data.remove(voting_data[0])

denver_info = voting_data[1]
voting_data.remove(voting_data[1])
voting_data.append(denver_info)

voting_data.append(arapahoe_info)

print(voting_data)

