# Challenge - Umbrella

![](https://images.unsplash.com/photo-1457131760772-7017c6180f05?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1036&q=80)

Every morning, Simone puts her umbrella in her bag.

Her day is divided in three parts : morning, afternoon and evening.
- She will take her umbrella out of her bag if, at any point of the day, the weather becomes `rainy` or a `thunderstorm`.
- She will keep her umbrella in her bag if the weather is `sunny` or `cloudy`.
- She will always start the day with the umbrella in her bag, no matter the previous day's weather.

Write a function that takes a list of weathers and returns how many times Simone will take her umbrella out of her bag.


**Examples**:
- `weather = ["rainy", "sunny", "rainy", "sunny", "rainy", "rainy"]` => Simone takes her umbrella out of her bag `3` times.
- `weather = ['sunny', 'cloudy', 'sunny', 'rainy', 'rainy', 'thunderstorm']` => Simone takes her umbrella out of her bag `1` time.
- `weather = ['rainy', 'rainy', 'rainy']` => Simone takes her umbrella out of her bag `1` time.
