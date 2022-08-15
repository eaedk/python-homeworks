from umbrella.solution import proposal

def test_valid():


    weathers = [["rainy", "sunny", "rainy", "sunny", "rainy", "rainy"],
    ['sunny', 'cloudy', 'sunny', 'rainy', 'rainy', 'thunderstorm'],
    ['rainy', 'rainy', 'rainy']
    ]
    solutions = [3, 1, 1,]
    results = []

    for weather in weathers:
        results.append(proposal(weather=weather))

    assert results == solutions

