// 스톱워치
const display = document.querySelector('#clock_display h3');
const startButton = document.querySelector(".btn.start");
const stopButton = document.querySelector(".btn.stop");
const resetButton = document.querySelector(".btn.reset");
const newRecordList = document.querySelector(".new_record");
const deleteButton = document.querySelector(".delete");
const totalRecordButton = document.querySelector(".total_record");

let startTime;
let beforeTime = 0;
let update;
let running = false;
let recordCount = 0;

// 스톱워치 형태로 변환
function timeFormat(time) {
    const minutes = Math.floor(time / 60000);
    const seconds = ((time % 60000) / 1000).toFixed(0);
    return `${minutes < 10 ? '0' : ''}${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
}

//타이머
const timeCheck = document.getElementById("time_check");
const clockDisplaySection = document.getElementById('clock_display');

function startTimer(duration) {
    let timeLeft = duration; // 남은 시간 (초)
    running = true;

    const timerInterval = setInterval(function () {
        if (timeLeft <= 0) {
            clearInterval(timerInterval);
            running = false;
            alert("시간이 다 되었습니다!"); // 알람 종료 창
            document.getElementById('clock_display').style.backgroundColor = "black"; // 배경색 변경
            setTimeout(() => {
                document.getElementById('clock_display').style.backgroundColor = ""; // 5초 후 원래상태로 돌아가기
            }, 5000); 
        } else {
            display.textContent = timeFormat(timeLeft * 1000); 
            timeLeft--;
        }
    }, 1000); 
}


// 1. start 누르면 시간 증가
function start() {
    if (!running) {
        // 타이머가 체크되어 있다면 타이머 시작
        if (timeCheck.checked) {
            startTimer(180); // 3분 
        } else {
            running = true;
            startTime = new Date() - beforeTime;
            update = setInterval(function () {
                beforeTime = new Date() - startTime;
                display.textContent = timeFormat(beforeTime);
            }, 1);
        }
    }
}


// 2-1 리스트에 기록 추가
function addRecord() {
    if (running) {
        const newRecord = document.createElement("li");
        newRecord.classList.add("new_record_list");

        const circleIcon = createSVGIcon("circle");
        const checkIcon = createSVGIcon("check-circle-fill");
        checkIcon.style.display = 'none';

        const timeRecord = document.createElement("p");
        timeRecord.textContent = timeFormat(beforeTime);

        newRecord.appendChild(circleIcon);
        newRecord.appendChild(checkIcon);
        newRecord.appendChild(timeRecord);

        const newRecordList = document.querySelector(".new_record");
        if (newRecordList) {
            newRecordList.appendChild(newRecord);
            recordCount++;
            updateTotalRecordButton(); // 전체 기록 수 업데이트
        } else {
            console.log("Error: newRecordList not found.");
        }
    }
}

function createSVGIcon(iconType) {  //체크되면 svg 바꾸기 위해서....
    const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    svg.setAttribute("xmlns", "http://www.w3.org/2000/svg");
    svg.setAttribute("width", "16");
    svg.setAttribute("height", "16");
    svg.setAttribute("fill", "currentColor");
    svg.setAttribute("class", `bi bi-${iconType}`);
    svg.setAttribute("viewBox", "0 0 16 16");

    const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
    if (iconType === "circle") {
        path.setAttribute("d", "M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16");
    } else if (iconType === "check-circle-fill") {
        path.setAttribute("d", "M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0m-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417l-2.093-2.094a.75.75 0 1 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 .708-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z");
    }
    svg.appendChild(path);
    return svg;
}

// 3. stop으로 시간 멈춤 & 기록 추가가
function stop() {
    if (running) {
        clearInterval(update);
        addRecord();
        running = false;
    }
}

// 기록 전체 삭제
function deleteAllRecords() {
    const deleteRecord = document.querySelectorAll(".new_record_list");
    deleteRecord.forEach(record => record.remove());
    recordCount = 0;
    updateTotalRecordButton(); 
}

// start, stop, reset, delete 버튼 활성화
startButton.addEventListener("click", start);
stopButton.addEventListener("click", stop);
resetButton.addEventListener("click", reset);
deleteButton.addEventListener("click", deleteSelectedRecords);

// 버튼 누르면 원 안에 체크 생성
document.querySelector('.new_record').addEventListener('click', function (event) {
    const listItem = event.target.closest('li');
    
    if (!listItem || !listItem.classList.contains('new_record_list')) return;

    const circleIcon = listItem.querySelector('.bi-circle');
    const checkIcon = listItem.querySelector('.bi-check-circle-fill');

    // 아이콘 상태
    if (circleIcon && checkIcon) {
        circleIcon.style.display = circleIcon.style.display === 'none' ? 'block' : 'none';
        checkIcon.style.display = checkIcon.style.display === 'none' ? 'block' : 'none';
        
        // 전체 선택 버튼 상태 업데이트
        updateTotalRecordButton();
    }
});

// 선택된 항목 삭제
function deleteSelectedRecords() {
    const records = document.querySelectorAll(".new_record_list");
    let deletedCount = 0;

    records.forEach(record => {
        const checkIcon = record.querySelector('.bi-check-circle-fill');
        // 체크 아이콘이 보이는 경우에만
        if (checkIcon && checkIcon.style.display === 'block') {
            record.remove();
            deletedCount++;
        }
    });
    
    // 삭제된 항목 개수에 따라 전체 기록 수 업데이트
    recordCount -= deletedCount;
    updateTotalRecordButton(); 
}


// 4. reset 누르면 시간, 리스트 초기화
function reset() {
    running = false;
    clearInterval(update);
    deleteAllRecords();
    display.textContent = "00:00";
    beforeTime = 0;
}

// 전체 선택 토글
function toggleAllRecords() {
    const records = document.querySelectorAll(".new_record_list");
    const totalChecked = totalRecordButton.querySelector('.bi-check-circle-fill').style.display === 'block';
    
    records.forEach(record => {
        const circleIcon = record.querySelector('.bi-circle');
        const checkIcon = record.querySelector('.bi-check-circle-fill');

        // 전체 선택 상태에 따라 아이콘 상태 변경
        circleIcon.style.display = totalChecked ? 'block' : 'none';
        checkIcon.style.display = totalChecked ? 'none' : 'block';
    });

    // 전체 선택 버튼 상태 업데이트
    updateTotalRecordButton();
}


// 전체 선택 버튼 상태 업데이트
function updateTotalRecordButton() {
    const records = document.querySelectorAll(".new_record_list");
    const totalCircle = totalRecordButton.querySelector('.bi-circle');
    const totalCheck = totalRecordButton.querySelector('.bi-check-circle-fill');

    // 모든 체크된 상태 확인
    const allChecked = Array.from(records).every(record => 
        record.querySelector('.bi-check-circle-fill').style.display === 'block'
    );

    // 전체 선택 버튼 상태 업데이트
    totalCircle.style.display = allChecked ? 'none' : 'block';
    totalCheck.style.display = allChecked ? 'block' : 'none';
}

// 이벤트 리스너 설정
totalRecordButton.addEventListener("click", toggleAllRecords);

// 초기 전체 선택 버튼 상태 설정
updateTotalRecordButton();



