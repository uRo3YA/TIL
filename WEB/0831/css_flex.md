

**position**

-----
- absolute 는 부모를 타고 올라가며, position이 static이 아닌 요소 중 먼저 발견한 요소를 기준으로 배치된다.
- fixed는 **기본적으로 viewport를 기준으로 배치**되지만, 조소 요상 중 **transform, perspective, filter 속성 중 하나라도 none이 아니면** 해당 요소를 기준으로 배치된다.
- z-index 값은 **position이 static이 아닌 경우에만 적용**된다. 그 외에도 flex와 grid에서도 적용된다.
- position 값이 absolute 혹은 fixed일 때 **display가 block으로 변경**된다.




**Flex Container**

-----
***1차원 레이아웃 구조를 만들 때 사용***

**display**

**flex**

- container가 **block 요소의 성질을 가짐**
- container들이 **수직으로 배치**되며, 가로로 늘어나는 특징을 가짐.

**inline-flex**

- 컨테이너가 **inline 요소의 성질을 가짐**
- container들이 **수평으로 배치**되며, item의 크기에 맞춰서 가로로 줄어드는 특징을 가짐.

**flex-direction**

***flex의 main-axis를 정하는 속성, 기본값은 row다.***

**row**

- **수평 방향으로 item을 나열**한다
- **왼쪽에서 오른쪽**으로 나열되며, row-reverse는 반대로 오른쪽에서 왼쪽으로 나열된다.

**column**

- **수직 방향으로 item을 나열**한다.
- **위쪽에서 아래쪽으로 나열**되며, column-reverse는 반대로 아래쪽에서 위쪽으로 나열된다.




**flex-wrap**

***flex의 줄바꿈을 처리하는 속성, 기본값은 nowrap이다.***

**nowrap**

- 줄바꿈을 하지 않는다.

**wrap**

- 줄바꿈이 가능하게 한다.

**wrap-reverse**

- 줄바꿈을 wrap과 반대로 처리한다.




**justify-content**

***main-axis의 정렬 방법을 정하는 속성, 기본값은 flex-start다.***

**flex-start**

- main-axis의 start 지점에 정렬한다

**flex-end**

- main-axis의 end 지점에 정렬한다

**center**

- main-axis의 가운데에 정렬한다.

**space-between**

- 첫 번째 item을 main-axis의 start 지점에, 마지막 item을 end 지점에 배치하고 **나머지 item은 남은 공간에 적절한 간격으로 정렬**한다.

**space-around**

- 각 item의 **양 옆에 공간을 적절히 분배해서 정렬**한다.




**align-items**

***cross-axis의 정렬 방법을 정하는 속성, item이 한 줄일 때 사용한다. 기본값은 stretch다.***

**stretch**

- item의 height가 컨테이너의 height에 맞춰서 늘어나도록 한다.
- item의 height를 명시해주면 **stretch 속성은 무시**된다.

**flex-start**

- cross-axis의 start 지점에 정렬한다.

**flex-end**

- cross-axis의 end 지점에 정렬한다.

**center**

- cross-axis의 가운데에 정렬한다.

**baseline**

- item의 **문자 기준선에 맞춰서 정렬**한다.




**align-content**

***align-item과 비슷하지만, item이 두 줄일 때 사용한다. 기본값은 stretch다.***

**flex-start**

- cross-axis의 start 지점에 정렬한다.

**flex-end**

- cross-axis의 end 지점에 정렬한다.

**center**

- cross-axis의 가운데에 정렬한다.

**space-between / space-around**

- 동작은 justify-content의 속성과 같지만, cross-axis를 기준으로 한다는 점이 다르다.




**Flex Item**

-----
**flex-grow**

***flex-item의 증가 너비 비율을 설정, 기본값은 0이다.***

- 비율을 정하는 기준은 **기본 너비를 제외한 나머지 영역**이다.
- 각 item의 비율을 일치시키고 싶다면 auto를 기준으로 하면 된다.




**flex-shrink**

***flex-item의 감소 너비 비율을 설정, 기본값은 1이다.***




**flex-basis**

***flex-item의 기본 너비를 설정한다. 기본값은 auto다.***

- flex-basis에 어떤 값을 주게 되면, 해당 요소에 설정되어있던 너비(width)가 무시된다.




**order**

***flex-item의 순서를 지정하는 속성, 값이 클수록 뒤에 배치된다. 기본값은 0이다.***

- HTML 구조를 변경하지 않고도 **item의 순서를 변경**할 수 있다.
- **음수도 사용**이 가능하다.




**align-self**

***flex-item에 개별적으로 cross-axis 정렬이 가능한 속성, 기본값은 auto이며, align-items의 값을 상속받는다.***

- **align-items가 사용하는 모든 속성**을 사용할 수 있다.