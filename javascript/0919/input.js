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