// 1. input 선택
const textInput = document.querySelector('#text-input')
// 2. input 이벤트 등록
textInput.addEventListener('input', function(e) {
    // input의 value를 받아오고 싶음
    // input은 이벤트의 대상!
    console.log(e)
    console.log(e.target.value)

    // 3. 그대로 출력하기
    document.getElementById("result_get").innerText = textInput.value;
    document.querySelector('#result_sel').innerText= textInput.value;
    
    document.getElementById("result_get_val").innerText = textInput;
    document.querySelector('#result_sel_val').innerText= textInput;
})

const nextBtn = document.querySelector('#nextBtn')
nextBtn.addEventListener('click',function(){
  const currentElement = document.querySelector('.active')
  const items = document.querySelectorAll('.carousel-item')
  const idx = [...items].indexOf(currentElement)
  console.log(currentElement,items,idx)
  currentElement.classList.toggle('active')
  items[(idx+1)%items.length].classList.toggle('active')
})
const pervBtn = document.querySelector('#pervBtn')
pervBtn.addEventListener('click',function(){
  const currentElement = document.querySelector('.active')
  const items = document.querySelectorAll('.carousel-item')
  const idx = [...items].indexOf(currentElement)
  console.log(currentElement,items,idx)
  currentElement.classList.toggle('active')
  items[(items.length+idx-1)%items.length].classList.toggle('active')
})

function test() {
    var p1 = document.getElementById('password1').value;
    var p2 = document.getElementById('password2').value;
    if( p1 != p2 ) {
        alert("비밀번호가 일치 하지 않습니다");
        return false;
    } else{
        alert("비밀번호가 일치합니다");
        return true;
    }
  }