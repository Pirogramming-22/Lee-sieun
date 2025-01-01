//json에서 item 받아오기
function loadItems(){
    return fetch('data/data.json').then(response => response.json())
    .then(json => console.log(json));
}



//main
loadItems()
    .then(items => {
        // displayItems(items);
        // setEventListners(items)
    })
.catch(console.log)