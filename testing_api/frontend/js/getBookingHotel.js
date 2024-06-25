
document.addEventListener('DOMContentLoaded', (event) => {
    const params = new URLSearchParams(window.location.search);
    const service_id = params.get('service_id');
    const check_in = document.getElementById('check_in');
    const check_out = document.getElementById('check_out');
    const room_id = document.getElementById('room_id');
    const total_price = document.getElementById('total_price');
    const room_price = document.getElementById('room_price')
    const room_type = document.getElementById('room_type')
    const provider_name = document.getElementById('provider_name')
    const rating = document.getElementById('rating')
    const image_wrapper = document.getElementById('image_wrapper')
    const check_in_date = document.getElementById('check_in_date')
    const check_out_date = document.getElementById('check_out_date')
    const total_night = document.getElementById('total_night')
    const count = document.getElementsByClassName('count')
    const room_price_1 = document.getElementById('room_price_1')

    let roomPriceValue = 0
    let providerName = ''

    console.log('check')

    async function getRoomData() {
        try {
            const response = await fetch(`http://52.200.174.164:8003/service/2`, {
                method: 'GET',
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            const result = await response.json()
            provider_name.innerHTML = result.data.provider_name
        } catch (error) {
            console.error('Error:', error);
        }
        try {
            const response = await fetch(`http://52.200.174.164:8003/hotel/room_type/${room_id}`, {
                method: 'GET',
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const result = await response.json();
            // console.log('Success:', result);
            console.log(result)
            room_price.innerHTML = `Rp. ${formatRupiah(result.price)}`
            room_type.innerHTML = result.type
            roomPriceValue = result.price
            provider_name.innerHTML = "Merlyn Hotel"
            image_wrapper.src = result.image
            room_price_1.innerHTML = `Rp. ${formatRupiah(result.price)}`

            updateTotalPrice()
        } catch (error) {
            console.error('Error:', error);
        }
    }
    const counterElement = document.getElementById('counter');
    const decreaseButton = document.getElementById('decrease');
    const increaseButton = document.getElementById('increase');

    let counterValue = 1;
    decreaseButton.addEventListener('click', () => {
        if (counterValue > 1) {
            counterValue--;
            counterElement.innerHTML = counterValue;
            updateTotalPrice();
        }
    });

    increaseButton.addEventListener('click', () => {
        counterValue++;
        counterElement.innerHTML = counterValue;
        updateTotalPrice();
    });

    function updateTotalPrice() {
        const totalPriceValue = roomPriceValue * counterValue;
        total_price.innerHTML = `Rp. ${formatRupiah(totalPriceValue)}`;
    }

    getRoomData()

});


function formatRupiah(number) {
    return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
}
