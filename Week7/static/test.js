// const dataurl = "http://127.0.0.1:3000/api/member?username=ply" // 明天確定api網址
// let info_list = [];
// let add = document.querySelector(".add") //抓一個id 叫做add的標籤



// fetch(dataurl)
//     .then(function(response){
        
//         return response.json()
// }).then(function(data){ //操作data

//     var info_list = data.data.name //  確認抓到資料再剖析資料
                    
//     add.innerHTML = info //把info 自料塞進標籤畫出來，或是用create element & getElementByid 去塞
    
          
// });



// const dataurl = "http://127.0.0.1:3000/api/member"

// function Postdata (dataurl, dataobject) {

//     return fetch(dataurl, {
//         body: JSON.stringify(),
//         cache: 'no-cache',
//         credentials: 'same-origin',
//         headers: {
//             // 'user-agent':  //找一下是啥鬼
//             'content-type': 'application/json'
//         },
//         method: 'POST',
//         mode: 'cors',
//         redirect: 'follow',
//         referrer: 'no-referrer',

//     }).then(response => response.json()

// )};

// const apiurl = "http://127.0.0.1:3000/api/member"

// fetch(dataurl,{


// }).then(function(response){
//     return response.json();

// }).then(function(data){
//     return_result = data.data.name
//     console.log(read);//印出我查找的username

//     //innerhtml 塞進去

// });






//先建立通訊

function senddata(url, dataobject){
    console.log(url);
    return fetch(url,).then(response => response.json())

};

//senddata通訊處理好 (fetchpart)

function submitsearch(){

   const x =  document.getElementById("username").value;
   const dataobject = {'data': x } // 確認
   console.log(dataobject)
   console.log("123")

   //寄出Json 到後端

    // senddata('http://127.0.0.1:3000/api/member?username=test', dataobject).then(dataobject => {
    //     console.log(dataobject); //印看看有沒有成功抓到後端來的資料
    //     var result = dataobject.name;
    //     document.getElementById("forinnerhtml").innerHTML = result; // 畫到前端

    // });



};

function senddataforupdate(url, dataobject){
    return fetch(url,{
        body:JSON.stringify(dataobject),
        headers:{
            'content-type':'applicaiton/json'
        },
        method: 'PATCH',

    }).then(response => response.json())

};

function transformresult(){
    if (result_for_updated == true)//要看一下是要怎麼抓"ok": true & "error": true

        return '更新成功';
    else
        return '更新失敗';


}


function submitchange(){

    const y =  document.getElementById("usernamechange").value;
    const dataobject = {'data': y } // 確認
    console.log(dataobject)

    //寄出（Patch)到後端
    senddata('http://127.0.0.1:3000/api/member', dataobject).then(dataobject => {
        console.log(dataobject); //印看看有沒有成功抓到後端來的資料
        const result_for_updated = dataobject.ok;
        console.log(transformresult(reuslt));// 看看是不是轉換成功

        document.getElementById("forupdatedinnerhtml").innerHTML = transformresult(reuslt);
       // 畫到前端

    });

 
 };



