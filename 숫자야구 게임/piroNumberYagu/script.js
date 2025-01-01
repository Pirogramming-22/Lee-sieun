//게임 초기화
// 1. 시도 가능 횟수 설정 (시도할 때마다 1씩 감소)
const totalAttempts = 9;
let remainingAttempts =totalAttempts;
document.getElementById('attempts').textContent = remainingAttempts;

// 2. 중복X의 랜덤 숫자 3개 생성 (0~9까지만)
const correctAnswer = Array.from({length:3},() => Math.floor(Math.random()*10)) //정답

// 3. html의 Input, 결과창 비우기
const submitBtn = document.getElementsByClassName('submit-button')[0];
const inputs = document.getElementsByClassName('input-field');
function resetInput(){
    for(let userinput of inputs){
        userinput.value = '';
        inputs[0].focus();
    }
}

//enter도 클릭으로 반영
const lastElement = inputs[inputs.length-1];
lastElement.addEventListener('keydown',(event)=>{
    if(event.key==='Enter'){
        submitBtn.click();
    }
})

// <숫자 확인>
function check_numbers(){
    //기회 모두 소진하면 실패
    if(remainingAttempts<=0){
        resetInput();
        document.getElementById('game-result-img').src = 'fail.png'
        return;
    }
    //시도 횟수 감소
    remainingAttempts--;
    document.getElementById('attempts').textContent = remainingAttempts;

    //사용자 값 입력 받기
    const num1 = document.getElementById('number1').value;
    const num2 = document.getElementById('number2').value;
    const num3 = document.getElementById('number3').value;

    const userAnswer = [num1, num2, num3];

    //s(자리 비교 후 같으면 증가), b(정답이 해당 숫자 포함하면 증가)
    let strike =0;
    let ball =0;
    userAnswer.forEach((num, index) => {
        const currentNum = parseInt(num, 10); 
        if(num == correctAnswer[index]){
            strike++;
        }else if(correctAnswer.includes(currentNum)){
            ball++;
        }
    });

    //s,b 결과 출력
    const resultDisplay = document.getElementById('results');
    if(strike === 0 && ball === 0){
        resultDisplay.innerHTML += `
        <div class="check-result">
            <span class="num-result">${userAnswer.join(' ')}</span>
            <i>:</i>
            <span class="result"><span class="out">0</span></span>
        </div>`;
        resetInput();
    }else{
        resultDisplay.innerHTML += ` 
        <div class="check-result">
            <span class="num-result">${userAnswer.join(' ')}</span>
            <i>:</i>
            <span class="result">
                <span>${strike} <span class="strike">S</span></span>
                <span>${ball} <span class="ball">B</span> </span>
            </span>
        </div>`;
        resetInput();
    }

    //시도 결과 출력
    if(strike===3){
        resetInput();
        document.getElementById('game-result-img').src = './success.png'
        submitBtn.disabled = true;
        return;
    }

    if(remainingAttempts === 0){
        resetInput();
        document.getElementById('game-result-img').src = 'fail.png'
        submitBtn.disabled = true;
    }
}


