function getCookie(c_name)
{
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
}

function addCard(title, opening, importance, date, id, main, closing, image, username){

    var openingCard = opening.slice(0, 100) + (opening.length > 100 ? "..." : ""); 

    var card = `
    <div class="cardblog">
        <div class="cardblog__header">
        <img src= ${image} alt="cardblog__image" class="cardblog__image" width="600">
        </div>
        <div class="cardblog__body">
        ${importance == "LW" ? '<span class="tagblog tag-green"> Low </span>' : ''}
        ${importance == "IM" ? '<span class="tagblog tag-yellow"> Intermediate </span>' : ''}
        ${importance == "HH" ? '<span class="tagblog tag-red"> High </span>' : ''}
        <a href = "${id}/" class = "cursor-pointer text-decoration-none text-black font-bold"> <h4>${title}</h4> </a>
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
            <div>
            <iconify-icon icon="typcn:edit" style = "color: #41b36a; font-size:32px; cursor:pointer;" onclick = "handleUpdateModal(${id})"></iconify-icon>
            <iconify-icon icon="typcn:trash" style = "color:#cb2d3e; font-size: 32px; cursor:pointer;" onclick = "handleDelete(${id})"></iconify-icon>
            </div>
        </div>
        </div>
    </div>

    <form method="PUT" action="/blogpost/update/" id = "idForm2-${id}">
        <div class="modal fade" id="exampleModal2-${id}" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header flex items-center">
                <h5 class="modal-title" id="exampleModalLabel">Update Blog</h5>
                    <span data-bs-dismiss="modal" aria-hidden="true" class = "text-2xl cursor-pointer">&times;</span>
                </button>
                </div>
                <div class="modal-body">
                <div class = "px-8">
                    <div class = "my-4">
                        <p class = "font-bold">Title </p>
                        <input type="text" placeholder="Title" class="form-control" id = "title2-${id}" required> </input>
                    
                    </div>
                            
                    <div class = "my-4">
                        <p class = "font-bold"> Opening Text </p>
                        <textarea id = "opening2-${id}" placeholder="Opening text ..." class="form-control" required></textarea>
                    </div>
                    
                    <div class = "my-4">
                    <p class = "font-bold"> Main Text </p>
                    <textarea id = "main2-${id}" placeholder="Main text ..." class="form-control" required></textarea>
                    </div>

                    <div class = "my-4">
                    <p class = "font-bold"> Closing Text </p>
                    <textarea id = "closing2-${id}" placeholder="Closing text ..." class="form-control" required></textarea>
                    </div>

                    <div class = "my-4">
                    <p class = "font-bold"> Importance </p>
                    <select id = "importance2-${id}" class="form-select" aria-label="Default select example">
                        <option value="LW"> Low </option>
                        <option value="IM"> Intermediate </option>
                        <option value="HH"> High </option>
                    </select>
                    </div>

                </div>
                </div>
                <div class="modal-footer flex flex-col items-center">
                <button type="submit" class="btn-addblogform"> Add </button>
                </div>
            </div>
            </div>
        </div>
    </form>
    `
    return card
}

function getUsername(id){
    $.ajax({
    type: "GET",
    url: `/blogpost/user/${id}`,
    async: false,  
    headers: { "X-CSRFToken": getCookie("csrftoken") },
    success: function(data){
        username = data.user
    }  
    })

    return username
}

function showData(){
    var importance = document.getElementById("importanceFilter").value;

    $.ajax({
    type: "GET",
    url: '/blogpost/json/',
    data:{
        importance:importance,
    },
    headers: { "X-CSRFToken": getCookie("csrftoken") },
    success: function(data){
        $('#containerBlog').html("");
        for(let i = 0; i < data.length ; i++){
            title = data[i].fields.title
            opening = data[i].fields.opening
            main = data[i].fields.main
            closing = data[i].fields.closing
            importance = data[i].fields.importance
            date = data[i].fields.time.substring(0, 10)
            user = data[i].fields.user
            id = data[i].pk
            username = getUsername(user)
            image = `https://source.unsplash.com/600x400/?$hiv/${id}`
            var card = addCard(title, opening, importance, date, id, main, closing, image, username)
            $(card).appendTo("#containerBlog")
        }
    }
    })
}

function handleUpdateModal(id){
    $(`#exampleModal2-${id}`).modal('toggle')
    $(`#idForm2-${id}`).submit(function(e){
    
    e.preventDefault()
    var form = $(this);
    var actionUrl = form.attr("action") + id + "/";
    var importance = document.getElementById(`importance2-${id}`).value;
    var title = $(`#title2-${id}`).val()
    var opening = $(`#opening2-${id}`).val()
    var main = $(`#main2-${id}`).val()
    var closing = $(`#closing2-${id}`).val()

    if(title.length > 100){
        alert("Title jangan panjang-panjang")
    }else{
        $.ajax({
        type: "PUT",
        url: actionUrl,
        data:{
            title: title,
            opening: opening,
            main: main,
            closing: closing,
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            importance:importance,
        },
        headers: { "X-CSRFToken": getCookie("csrftoken") },
        success: function(data){
            showData()
            showAttr()
            $(`#exampleModal2-${id}`).modal('hide')
        }, 
        error: function(error){
            alert(error.responseJSON.message)
        }
        })
    }
    })
}

function handleDelete(id){
    actionUrl = `/blogpost/delete/${id}`
    $.ajax({
    type: "DELETE",
    url: actionUrl, 
    success: function(data){
        $('#div').html("");
        showData()
    },  
    headers: { "X-CSRFToken": getCookie("csrftoken") },
    error: function(error){
        alert(error.responseJSON.error)
    }
    })
}

$(document).ready(function(){
    showData()
    showAttr()
})

$("#idForm").submit(function(e){
    e.preventDefault()
    var form = $(this);
    var actionUrl = form.attr("action");
    var importance = document.getElementById("importance").value;
    var title = $('#title').val()
    var opening = $("#opening").val()
    var main = $("#main").val()
    var closing = $("#closing").val()

    if(title.length > 50){
    alert("Title jangan panjang-panjang")
    }else{
    $.ajax({
        type: "POST",
        url: actionUrl,
        data:{
        title: title,
        opening: opening,
        main: main,
        closing: closing,
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        importance:importance,
        },
        headers: { "X-CSRFToken": getCookie("csrftoken") },
        success: function(data){
        showData()
        $("#exampleModal").modal('hide')
        $("#title").val("");
        $("#opening").val("");
        $("#main").val("");
        $("#closing").val("");
        $("#importance").val("LW");
        }, 
        error: function(error){
        alert(error.responseJSON.error)
        }
    })
    }
})

function showAttr(){
    var importance = document.getElementById("importanceFilter").value;
    $.ajax({
    type: "GET",
    url: '/blogpost/json/',
    data:{
        importance:importance,
    },
    headers: { "X-CSRFToken": getCookie("csrftoken") },
    success: function(data){
        for(let i = 0; i < data.length ; i++){
            title = data[i].fields.title
            opening = data[i].fields.opening
            main = data[i].fields.main
            closing = data[i].fields.closing
            importance = data[i].fields.importance
            date = data[i].fields.time.substring(0, 10)
            id = data[i].pk

            $(`#importance2-${id}`).val(importance);
            $(`#title2-${id}`).val(title)
            $(`#opening2-${id}`).val(opening)
            $(`#main2-${id}`).val(main)
            $(`#closing2-${id}`).val(closing)
        }
    }
    })
}

$('#importanceFilter').change(function () {  
    showData() 
})
