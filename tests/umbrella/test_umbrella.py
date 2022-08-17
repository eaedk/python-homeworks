from umbrella.solution import proposal

def test_valid():

    weathers = [["rainy", "sunny", "rainy", "sunny", "rainy", "rainy"],
    ['sunny', 'cloudy', 'sunny', 'rainy', 'rainy', 'thunderstorm'],
    ['rainy', 'rainy', 'rainy'],
    ['sunny', 'cloudy', 'rainy', 'rainy', 'rainy', 'thunderstorm'],
    ]
    solutions = [3, 1, 1, 2]
    results = []

    for weather in weathers:
        results.append(proposal(weather=weather))

    assert results == solutions

