import pygal

from die import Die

# Cria um D6
die = Die()
die_00 = Die()
die_01 = Die()
die_02 = Die()

# Faz alguns lançamentos e armazena os resultados em uma lista
results = []
for roll_num in range(50000):
    result = die_00.roll() + die_01.roll() + die_02.roll()
    results.append(result)

# Analisa os resultados
frequencies = []
min_result = 3
max_result = die_00.num_sides + die_01.num_sides + die_02.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualiza os resultados
hist = pygal.Bar()

hist.title = "Results of rolling three D6 50,000 times."

list_x_labels = die.gera_list_labels_x(min_result, max_result)
hist.x_labels = list_x_labels
hist.x_title = "Results"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('dice_three_D6_visual.svg')