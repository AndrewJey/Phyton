function getProducts(){
    $.ajax({
        type: "GET",
        url: "http://localhost:8080/products.json",
        dataType: "json",
        success: function (data) {
            data=JSON.stringify(data);
            data=JSON.parse(data);
            console.log(data);
            var table='<table id="products" class="table">'+
                '<tr><td><strong>Fecha</strong></td>'+
                '<td><strong>Compra</strong></td>'+
                '<td><strong>Venta</strong></td>' +
                '<td><strong>Create</strong></td>'+
                '<td><strong>Edit</strong></td>'+
                '</tr>';
            console.log(data.length);
            for (var i=0; i < data.length; i++){
                table=table+'<tr><td>'+data[i].id+'</td>'+
                             '<td>'+data[i].name+'</td>'+
                             '<td>'+data[i].price+'</td>'+
                             '<td><a href="products/edit/'+data[i].id+'"><button>Edit</button></a>'+
                             '<td><a href="products/edit/'+data[i].id+'"><button>Edit</button></a></tr>';

            }
            table=table+'</table>';
            document.getElementById("products").innerHTML=table;
        },
        error: function (jqXHR, textStatus) {
            console.log(textStatus);
        }

    });
}