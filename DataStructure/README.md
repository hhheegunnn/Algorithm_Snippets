<h1 align="center">Data Structure</h1>
<p align="center">

- <u>**_수정_**</u>


<br>
<br>

## 우선순위 큐(Priority Queue)

- **우선순위가 가장 높은 데이터를 가장 먼저 삭제**하는 자료구조
- 표준 라이브러리 형태로 지원
```python
>>> import heapq
```
- heap
    - 우선순위 큐를 구현하기 위해 사용하는 자료구조 중 하나
    - 최소 힙(Min heap)과 최대 힙(Max heap)
    - 다익스트라 최단 경로 알고리즘을 포함한 다양한 알고리즘에 사용
    - 삽입 시간 **_O(logN)_**, 삭제 시간 **_O(logN)_**

```python
>>> iterable = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
>>> print(heapsort(iterable))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
<br>

