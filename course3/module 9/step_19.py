def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    answer = {'name': grades['name'], 'top_grade': max(grades['grades'])}
    return answer

print(*top_grade.__annotations__.values())
