def solution(gems):
    gem_types = len(set(gems))
    gem_count = {}

    left = 0
    answer = [0, len(gems) - 1]

    for right in range(len(gems)):
        gem_count[gems[right]] = gem_count.get(gems[right], 0) + 1

        while len(gem_count) == gem_types:
            if right - left < answer[1] - answer[0]:
                answer = [left, right]

            gem_count[gems[left]] -= 1

            if gem_count[gems[left]] == 0:
                del gem_count[gems[left]]

            left += 1

    return [answer[0] + 1, answer[1] + 1]