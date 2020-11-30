# Sorting

- <u>**_데이터를 특정한 기준에 따라 순서대로 나열하는 것_**</u>



## 선택정렬 (Selection sort)

- 처리되지 않은 데이터 중에서 가장 작은 데이터를 **선택**해 맨 앞에 있는 데이터와 바꾸는 것을 반복

```python
selection_sort(array)
```

| Best | Average | Worst | Memory | Stable | Method     |
| ---- | ------- | ----- | ----------------- | ------ | ---------- |
| <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/ac9810bbdafe4a6a8061338db0f74e25b7952620">  | <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/ac9810bbdafe4a6a8061338db0f74e25b7952620">   | <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/ac9810bbdafe4a6a8061338db0f74e25b7952620"> | 1 (In-place)      | **No**    | Selection |



## GCD (Greatest Common Divisor)

### 유클리드 호제법
- 두 개의 자연수에 대한 최대공약수를 구하는 대표적인 알고리즘
- 두 자연수 A, B에 대하여 (A>B) A를 B로 나눈 나머지를 R
- 이때 A와 B의 최대공약수는 B와 R의 최대공약수와 동일
- 유클리드 호제법의 아이디어를 그대로 재귀 함수로 작성 가능
    - 예시 : GCD(192,162)

        | Step | A | B |
        | :----: | :-: | :-: |
        | 1 | 192 | 162 |
        | 2 | 162 | 30 |
        | 3 | 30 | 12 |
        | 4 | 12 | 6 |





