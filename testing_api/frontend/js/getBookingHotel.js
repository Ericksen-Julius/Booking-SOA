
document.addEventListener('DOMContentLoaded', (event) => {
    const params = new URLSearchParams(window.location.search);
    const service_id = params.get('service_id');
    const check_in = params.get('checkin');
    const check_out = params.get('checkout');
    const room_id = params.get('room_id');
    const total_price = document.getElementById('total_price');
    const room_price = document.getElementById('room_price')
    const room_type = document.getElementById('room_type')
    const provider_name = document.getElementById('provider_name')
    const rating = document.getElementById('rating')
    const image_wrapper = document.getElementById('image_wrapper')
    const check_in_date = document.getElementById('check_in_date')
    const check_out_date = document.getElementById('check_out_date')
    const total_night = document.getElementById('total_night')
    const count = document.getElementById('count')
    const room_price_1 = document.getElementById('room_price1')
    const service_url = ''
    let roomPriceValue = 0
    let providerName = 'Merlyn Hotel'

    console.log(check_in)
    console.log(check_out)
    console.log(service_id)
    console.log(room_id)


    const dateObjectCheckIn = new Date(check_in);
    const dateObjectCheckOut = new Date(check_out);

    const days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
    const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

    const dayOfWeekCheckIn = days[dateObjectCheckIn.getDay()];
    const dayOfMonthCheckIn = dateObjectCheckIn.getDate();
    const monthCheckIn = months[dateObjectCheckIn.getMonth()];
    const yearCheckIn = dateObjectCheckIn.getFullYear();
    const dayOfWeekCheckOut = days[dateObjectCheckOut.getDay()];
    const dayOfMonthCheckOut = dateObjectCheckOut.getDate();
    const monthCheckOut = months[dateObjectCheckOut.getMonth()];
    const yearCheckOut = dateObjectCheckOut.getFullYear();

    check_in_date.innerHTML = `${dayOfWeekCheckIn}, ${dayOfMonthCheckIn} ${monthCheckIn} ${yearCheckIn}`;
    check_out_date.innerHTML = `${dayOfWeekCheckOut}, ${dayOfMonthCheckOut} ${monthCheckOut} ${yearCheckOut}`;

    const checkIn = new Date(check_in);
    const checkOut = new Date(check_out);

    const differenceMs = Math.abs(checkOut - checkIn);

    const totalNights = Math.ceil(differenceMs / (1000 * 60 * 60 * 24));

    total_night.innerHTML = totalNights == 1 ? `(${totalNights} night)` : `(${totalNights} night)`


    // async function getRoomData() {
    //     try {
    //         const response = await fetch(`http://52.200.174.164:8003/service/${service_id}`, {
    //             method: 'GET',
    //         });

    //         if (!response.ok) {
    //             throw new Error(`HTTP error! Status: ${response.status}`);
    //         }
    //         const result = await response.json()
    //         provider_name.innerHTML = result.data.provider_name
    //         service_url = result.data.service_url

    //     } catch (error) {
    //         console.error('Error:', error);
    //     }

    //     try {
    //         const response = await fetch(`http://localhost:8000/reviewRating/${providerName}`, {
    //             method: 'GET',
    //         });

    //         if (!response.ok) {
    //             throw new Error(`HTTP error! Status: ${response.status}`);
    //         }
    //         const result = await response.json()
    //         console.log(result)
    // rating.innerHTML = `${result.average_rating}/5 <span
    //                     class="text-dark">(${result.total_reviewers})</span>`
    //     } catch (error) {
    //         console.error('Error:', error);
    //     }

    //     try {
    //         const url = `${service_url}/hotel/room_type/${room_id}`
    //         const response = await fetch(`http://52.200.174.164:8003/hotel/room_type/1`, {
    //             method: 'GET',
    //         });

    //         if (!response.ok) {
    //             throw new Error(`HTTP error! Status: ${response.status}`);
    //         }

    //         const result = await response.json();
    //         // console.log('Success:', result);
    //         console.log(result)
    //         room_price.innerHTML = `Rp. ${formatRupiah(result.price)}`
    //         room_type.innerHTML = result.type
    //         roomPriceValue = result.price
    //         provider_name.innerHTML = providerName
    //         image_wrapper.src = result.image
    //         room_price_1.innerHTML = `Rp. ${formatRupiah(result.price)}`
    //         count.innerHTML = `(${counterValue}x)`

    //         updateTotalPrice()
    //     } catch (error) {
    //         console.error('Error:', error);
    //     }
    // }
    const counterElement = document.getElementById('counter');
    const decreaseButton = document.getElementById('decrease');
    const increaseButton = document.getElementById('increase');

    let counterValue = 1;
    decreaseButton.addEventListener('click', () => {
        if (counterValue > 1) {
            counterValue--;
            counterElement.innerHTML = counterValue;
            count.innerHTML = `(${counterValue}x)`
            updateTotalPrice();
        }
    });

    increaseButton.addEventListener('click', () => {
        counterValue++;
        counterElement.innerHTML = counterValue;
        count.innerHTML = `(${counterValue}x)`
        updateTotalPrice();
    });

    function updateTotalPrice() {
        const totalPriceValue = roomPriceValue * counterValue;
        total_price.innerHTML = `Rp. ${formatRupiah(totalPriceValue)}`;
    }
    // getRoomData()

});


function formatRupiah(number) {
    return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
}
