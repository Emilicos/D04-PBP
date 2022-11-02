function getUsername(id){
    $.ajax({
      type: "GET",
      url: `/blogpost/user/${id}`,
      async: false,  
      success: function(data){
        username = data.user
      }  
    })

    return username
}

function myFunction(){  
var element = document.getElementById('support');
var value = element.innerHTML; 
++value;
console.log(value)
document.getElementById('support').innerHTML = value;
localStorage.setItem('support', value)
}

function myFunction2(){
document.getElementById('support').innerHTML = localStorage.getItem('mynumber');
}

function showBlogpost(){
$.ajax({
  type: "GET",
  url: "/blogpost/json/?importance=DT", 
  success: function(data){
    blogs = data.reverse()
    var card = ""
    if(blogs.length == 0){
        card = `<h1> Belum ada </h1>`
        $(card).appendTo("#containerBlog")
    }else if(blogs.length == 1){
        title = data[0].fields.title
        opening = data[0].fields.opening
        main = data[0].fields.main
        closing = data[0].fields.closing
        importance = data[0].fields.importance
        date = data[0].fields.time.substring(0, 10)
        user = data[0].fields.user
        id = data[0].pk
        username = getUsername(user)
        var openingCard = opening.slice(0, 100) + (opening.length > 100 ? "..." : ""); 
        image = `https://source.unsplash.com/600x400/?$hiv/${id}`
        card = 
        `
          <div class="cardblog">
            <div class="cardblog__header">
              <img src= ${image} alt="cardblog__image" class="cardblog__image" width="600">
            </div>
            <div class="cardblog__body">
              ${importance == "LW" ? '<span class="tagblog tag-green"> Low </span>' : ''}
              ${importance == "IM" ? '<span class="tagblog tag-yellow"> Intermediate </span>' : ''}
              ${importance == "HH" ? '<span class="tagblog tag-red"> High </span>' : ''}
              <a href = "/blogpost/${id}/" class = "cursor-pointer text-decoration-none text-black font-bold"> <h4>${title}</h4> </a>
              <p> ${openingCard} </p>
            </div>
            <div class="cardblog__footer">
              <div class="userblog">
                <div class="userblog__info">
                  <img src="https://img.lovepik.com/element/45000/4103.png_860.png" alt="userblog__image" class="userblog__image" width = "50px" height = "50px">
                  <div style = "max-width: 150px; width: 100%;">
                    <h5 class = "capitalize"> ${username} </h5>
                    <small> ${date} </small>
                  </div>
                </div>
              </div>
            </div>
          </div>
        `
        $(card).appendTo("#containerBlog")
    }else if(data.length >= 2){
      for(let i = 0; i < 2 ; i++){
        title = data[i].fields.title
        opening = data[i].fields.opening
        main = data[i].fields.main
        closing = data[i].fields.closing
        importance = data[i].fields.importance
        date = data[i].fields.time.substring(0, 10)
        user = data[i].fields.user
        id = data[i].pk
        username = getUsername(user)
        var openingCard = opening.slice(0, 100) + (opening.length > 100 ? "..." : ""); 
        image = `https://source.unsplash.com/600x400/?$hiv/${id}`

        card = 
        `
          <div class="cardblog show-${i}">
            <div class="cardblog__header">
              <img src= ${image} alt="cardblog__image" class="cardblog__image" width="600">
            </div>
            <div class="cardblog__body">
              ${importance == "LW" ? '<span class="tagblog tag-green"> Low </span>' : ''}
              ${importance == "IM" ? '<span class="tagblog tag-yellow"> Intermediate </span>' : ''}
              ${importance == "HH" ? '<span class="tagblog tag-red"> High </span>' : ''}
              <a href = "/blogpost/${id}/" class = "cursor-pointer text-decoration-none text-black font-bold"> <h4>${title}</h4> </a>
              <p> ${openingCard} </p>
            </div>
            <div class="cardblog__footer">
              <div class="userblog">
                <div class="userblog__info">
                  <img src="https://img.lovepik.com/element/45000/4103.png_860.png" alt="userblog__image" class="userblog__image" width = "50px" height = "50px">
                  <div style = "max-width: 150px; width: 100%;">
                    <h5 class = "capitalize"> ${username} </h5>
                    <small> ${date} </small>
                  </div>
                </div>
              </div>
            </div>
          </div>
        `
        $(card).appendTo("#containerBlog")
      }
    }
  }
})
}

$(document).ready(function(){
myFunction2();
showBlogpost();
})