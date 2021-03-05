function abc(tag){
    let num = tag.parentNode.parentNode.querySelector('td').textContent;
    console.log(num);

    fetch(hostip+'/inquiry_data_num/'+num, {
        "method": "GET"
    })
    .then(res => res.json())
    .then((res) => {
        console.log(res);
        let target = document.querySelector("#Hide").querySelector("div");
        target.innerHTML = "";
        for (let data of res['data']) {
            let cont = `
                <!-- Post Content Column -->
                <div class="col-lg-8">

                    <!-- Title -->
                    <h4 class="mt-4">${data['title']}</h4>
                    <hr>

                    <!-- Date/Time -->
                    <p>${data['time']}</p>

                    <hr>


                    <!-- Post Content -->
                    <blockquote class="blockquote">
                        <p class="mb-0">${data['comment']}</p>
                        <footer class="blockquote-footer">
                        <cite title="Source Title">${data['u_id']}</cite>
                        </footer>
                    </blockquote>

                    <hr>

                </div>

                <div id="paging">
                    <a href="javascript:display()">목록</a>
                </div>
            `;
        target.insertAdjacentHTML("beforeend", cont);
        }
    })
}

function reservation(){
    let target = document.querySelector("div").querySelector("form");
    let num= localStorage.getItem("knum");
    let cont=`
            <input type="text" name= "Latitude" placeholder="Latitude"/>
            <input type="text" name= "Longtitude" placeholder="Longtitude"/>
            <input type="hidden" name="knum" value="${num}">
            <input type="submit" name="a" value="반납"><input type="submit" name="a" value="고장">
    `;
    target.insertAdjacentHTML("beforeend", cont);
}

function broken(){
    if(confirm('고장났습니까?')){
        let num=localStorage.getItem("knum");
        fetch(hostip+'/broken_data/'+num, {
            'Content-Type': 'application/json',
            "method": "GET"
        })
        location.href="/";
        } else {
            location.href = "/reservation";
            return false;
        }
}

function admin_fixed(tag){
    let num = tag.parentNode.parentNode.querySelector('td').textContent;
    localStorage.setItem("knum",num);
}
function admin(){
    fetch(hostip+"/admin_data", {
        'Content-Type': 'application/json',
        'method': "GET",
    })
    .then(res => res.json())
    .then((res)=> {
        console.log(res);
        let target = document.querySelector("#show").querySelector("tbody");
        for (let data of res['data']) {
            let cont = `
            <tr>
                <td><a href="/admin_fix" onclick=admin_fixed(this)>${data['K_ID']}</a></td>
                <td>${data['Battery']}</td>
                <td>${data['Latitude']}</td>
                <td>${data['Longtitude']}</td>
                <td>${data['Broken']}</td>
                <td>${data['U_ID']}</td>
                <td>${data['Used']}</td>
                <td>${data['time']}</td>
            </tr>
            `;
            target.insertAdjacentHTML("beforeend", cont);
        }
    });
}

function admin_fix(){
    let target = document.querySelector("div").querySelector("form");
    let num= localStorage.getItem("knum");
    console.log(num);
    let cont=`
            <input type="text" name= "battery" placeholder="battery"/>
            <input type="text" name= "Latitude" placeholder="Latitude"/>
            <input type="text" name= "Longtitude" placeholder="Longtitude"/>
            <input type="text" name= "broken" placeholder="broken"/>
            <input type="hidden" name="knum" value="${num}">
            <button type="submit">고침</button>
    `;
    target.insertAdjacentHTML("beforeend", cont);
}

function inq(){
    fetch(hostip+"/inquiry_data", {
        'Content-Type': 'application/json',
        'method': "GET",
    })
    .then(res => res.json())
    .then((res)=> {
        console.log(res);
        let target = document.querySelector("#show").querySelector("tbody");
        for (let data of res['data']) {
            let cont = `
            <tr>
                <td>${data['num']}</td>
                <td id="title">
                <a href="javascript:display()" onclick="abc(this)">${data['title']}</a>
                </td>
                <td>${data['u_id']}</td>
                <td>${data['time']}</td>
            </tr>
            `;
            target.insertAdjacentHTML("beforeend", cont);
        }
    });

}
function ttt(){
    let num1=localStorage.getItem("knum");
    console.log(num1);
    fetch(hostip+'/pay_data/'+num1, {
        'Content-Type': 'application/json',
        "method": "GET"
    })
}

function clickyes(tag){
    if(confirm('예약하시겠습니까?')){
    let num = tag.parentNode.parentNode.querySelector('td').textContent;
    console.log(num);
    localStorage.setItem("knum", num);
    fetch(hostip+'/select_kickboard_data_num/'+num, {
        'Content-Type': 'application/json',
        "method": "GET"
    })
    location.href="reservation";
    } else {
        location.href = "select_kickboard";
        return false;
    }
}


function paypage(){
    let num= localStorage.getItem("knum");
    fetch(hostip+"/pay_data/"+num, {
        'Content-Type': 'application/json',
        'method': "GET",
    })
    .then(res => res.json())
    .then((res)=> {
        console.log(res);
        let target = document.querySelector("#kick").querySelector("div");
        let data =res['data'];
            distance = Math.round(data['distance']*1000)/1000;
            let cont = `
            <h1>이용시간은 ${data['borrowed_time']}초</h1>
            <h1>결제 금액은 ${data['payment']}원</h1>
            <h1>이동거리는 ${distance}km</h1>
            <button onclick="home()">확인</button><button onclick="mypage()">마이페이지</button>
            `;
            target.insertAdjacentHTML("beforeend", cont);
    });
}
function home(){
    location.href="/";
}
function mypage(){
    location.href="/mypage";
}

function kick_log(){
    let num1 = localStorage.getItem("lat1");
    let num2 = localStorage.getItem("lon1");
    console.log(num1);
    console.log(num2);
    fetch(hostip+"/select_kickboard_data", {
        'Content-Type': 'application/json',
        'method': "GET",
    })
    .then(res => res.json())
    .then((res)=> {
        console.log(res);
        let target = document.querySelector("#show").querySelector("tbody");
        for (let data of res['data']) {
            function deg2rad(deg) {
                return deg * (Math.PI/180);
            }
            let r= 6371;
            console.log(typeof data['latitude']);
            let dLat = deg2rad(num1-data['latitude']);
            let dLon = deg2rad(num2-data['longtitude']);
            console.log(dLat);
            console.log(dLon);
            let a=
                Math.sin(dLat/2) * Math.sin(dLat/2) + Math.cos(deg2rad(num1)) * Math.cos(deg2rad(data['latitude'])) * Math.sin(dLon/2) * Math.sin(dLon/2);
            let c=2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
            let d= r * c;
            let distance=Math.round(d*1000)/1000;
            let cont = `
            <tr>
                
                <td class = "look"><a onclick="clickyes(this)">${data['k_id']}</a></td>
                <td>${distance}km</td>
            </tr>
            `;
            target.insertAdjacentHTML("beforeend", cont);
        }
    });

}


function display(){ 
    if(document.getElementById("Hide").style.display == 'none'){
      document.getElementById("Hide").style.display = 'block';
      document.getElementById("write").style.display = 'none';
      document.getElementById("show").style.display = 'none';
    }
    else{
    document.getElementById("show").style.display = 'block';
    document.getElementById("Hide").style.display = 'none';
    document.getElementById("write").style.display = 'block';
}}

