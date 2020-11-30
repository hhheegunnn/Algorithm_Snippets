<h1 align="center">Sorting algorithm</h1>
<p align="center">

- <u>**_데이터를 특정한 기준에 따라 순서대로 나열하는 것_**</u>




## 선택정렬 (Selection sort)

- 처리되지 않은 데이터 중에서 가장 작은 데이터를 **_선택_** 해 맨 앞에 있는 데이터와 바꾸는 것을 반복
- *N*번 만큼 가장 작은 수를 찾아서 맨 앞으로 보냄
- 구현 방식에 따라 사소한 오차는 있을 수 있지만, 정체 연산 횟수는 다음과 같다.
    - *N + (N-1) + (N-2) + ... + 2*
- 이는 *(N\*\*2+N-2)/2*로 표현, -> **_O(N\*\*2)_**

```python
>>> array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
>>> selection_sort(array)
step 0 [0, 5, 9, 7, 3, 1, 6, 2, 4, 8]
step 1 [0, 1, 9, 7, 3, 5, 6, 2, 4, 8]
step 2 [0, 1, 2, 7, 3, 5, 6, 9, 4, 8]
step 3 [0, 1, 2, 3, 7, 5, 6, 9, 4, 8]
step 4 [0, 1, 2, 3, 4, 5, 6, 9, 7, 8]
step 5 [0, 1, 2, 3, 4, 5, 6, 9, 7, 8]
step 6 [0, 1, 2, 3, 4, 5, 6, 9, 7, 8]
step 7 [0, 1, 2, 3, 4, 5, 6, 7, 9, 8]
step 8 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
step 9 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
![Alt text](/img/selection_sort.jpg)

| Best | Average | Worst | Memory | Stable | Method     |
| ---- | ------- | ----- | ----------------- | ------ | ---------- |
| <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/ac9810bbdafe4a6a8061338db0f74e25b7952620">  | <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/ac9810bbdafe4a6a8061338db0f74e25b7952620">   | <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/ac9810bbdafe4a6a8061338db0f74e25b7952620"> | 1 (In-place)      | **No**    | Selection |


## 삽입정렬 (Insertion sort)

- 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 **_삽입_**
- 선택 정렬 비해 구현 난이도가 높은 편이지만, 일반적으로 더 효율적으로 동작
- 시간 복잡도는 **_O(N\*\*2)_** 이며, 선택 정렬과 마찬가지로 반복문이 두 번 중첩
- 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작
    - 최선의 경우 *O(N)* 의 시간 복잡도

```python
>>> array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
>>> insertion_sort(array)
step 1 [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
step 2 [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
step 3 [0, 5, 7, 9, 3, 1, 6, 2, 4, 8]
step 4 [0, 3, 5, 7, 9, 1, 6, 2, 4, 8]
step 5 [0, 1, 3, 5, 7, 9, 6, 2, 4, 8]
step 6 [0, 1, 3, 5, 6, 7, 9, 2, 4, 8]
step 7 [0, 1, 2, 3, 5, 6, 7, 9, 4, 8]
step 8 [0, 1, 2, 3, 4, 5, 6, 7, 9, 8]
step 9 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

| Best | Average | Worst | Memory | Stable | Method     |
| ---- | ------- | ----- | ----------------- | ------ | ---------- |
| <i>n</i> | <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/ac9810bbdafe4a6a8061338db0f74e25b7952620">   | <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/ac9810bbdafe4a6a8061338db0f74e25b7952620"> | 1 (In-place)      | Yes    | Insertion |






