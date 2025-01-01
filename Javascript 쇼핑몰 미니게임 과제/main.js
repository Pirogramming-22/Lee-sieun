//json에서 item 받아오기 -> 받아오는 걸 성공하면 json 타입으로 변경
function loadItems(){
    return fetch('data/data.json')
    .then(response => response.json())
    .then(json => json.items);
}

//items를 list로 업데이트트
function displayItems(items){
    const container = document.querySelector('.items');
    container.innerHTML = items.map(item => createHTMLString(item)).join('');
}

//주어진 item에서 HTML list를 생성함함
function createHTMLString(item){
    return `
    <li class="item">
            <img src="${item.image}" alt="${item.type}" class="item_thumbnail">
            <span class="item__description">${item.gender}, ${item.size}</span>
        </li>
    `;
}

function onButtonClick(event, items){
    const dataset = event.target.dataset;
    const key = dataset.key;
    const value =dataset.value;

    if(key == null || value == null){
        return;
    }
    //key가 들어있을 때만 작동하게 만듦
    displayItems(items.filter(item => item[key] === value))
}



function setEventListners(items){
    const logo = document.querySelector('.logo');
    const buttos = document.querySelector('.buttons');
    logo.addEventListener('click',() => displayItems(items));
    buttos.addEventListener('click', event => onButtonClick(event,items))
}

//main
loadItems()
    .then(items => {
        displayItems(items);
        setEventListners(items)
    })
.catch(console.log)