
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

function showData(id){
    $.ajax({
        type: "GET",
        url: `/blogpost/json/${id}`,
        success: function(data){
            console.log(data)
            $('#artikelBlog').html("");
            title = data[0].fields.title
            $('title').html(title);
            opening = data[0].fields.opening
            main = data[0].fields.main
            closing = data[0].fields.closing
            importance = data[0].fields.importance
            user = data[0].fields.user
            username = getUsername(user)
            let importanceIndicator
            if(importance == "HH"){
                importanceIndicator = "High"
            }else if(importance == "IM"){
                importanceIndicator = "Intermediate"
            }else{
                importanceIndicator = "Low"
            }
            date = data[0].fields.time.substring(0, 10)

            var artikel = `
                <h1 class = "text-4xl font-bold"> ${title} </h1>
                <div class = "flex justify-between">
                    <h2 class = "text-xl font-bold" style = "color:#GBGE70;"> ${date} </h2>
                    <h2 class = "text-xl font-bold" style = "color:${importance == "HH" ? "#cb2d3e" : ""} ${importance == "IM" ? "#D1913C" : ""} ${importance == "LW" ? "#41b36a" : ""} ;"> ${importanceIndicator} </h2>
                </div>
                <h2 class = "text-left"> Made by: ${username} </h2>
                <p class = "text-2xl text-left line-height"> ${opening} </p>
                <p class = "text-2xl text-left line-height"> ${main} </p>
                <p class = "text-2xl text-left line-height"> ${closing} </p>
            `

            $(artikel).appendTo("#artikelBlog")

        }
    })
}

$(document).ready(function(){
    url = window.location.pathname
    const urls = url.split("/");
    showData(Number(urls[urls.length - 2]))
})