$.ajax({
    type:"GET",
    url:'/order/load_order_data/',
    success: function(response){
        // const data = JSON.parse(data)
        // console.log((response))
        const data= response.data
        console.log(data)
        // data = JSON.parse(data);
        // const priceElemetn = document.getElementById('price')

        data.forEach(el => {
            console.log(el)

            $("#sku_list").append(new Option(el.sku, el.sku));
        })

        console.log('id', $('#sku_list'))

        $('#sku_list').on('change', function (e) {
            console.log('sku value', this.value)

            const selectedSku = Object.values(data).filter(data => data.sku === this.value);
            console.log('selec sku', selectedSku) 
            console.log('selec sku[0]', selectedSku[0]) 
            $('#price').val(selectedSku[0].sell_price);
        
        });

        
    },
    error: function(error) {
        console.log('error', error)
    }


})

