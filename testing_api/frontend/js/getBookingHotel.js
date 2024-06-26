
document.addEventListener('DOMContentLoaded', function () {
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
    let service_url = ''
    const submitButton = document.getElementById('book')
    let roomPriceValue = 0
    let counterValue = 1
    let totalPriceValue = roomPriceValue * counterValue;
    let providerName = 'Merlyn Hotel'

    console.log(check_in)
    console.log(check_out)
    console.log(service_id)
    console.log(room_id)
    if (!room_id || !check_in || !check_out || !service_id) {
        document.body.innerHTML = '<h1>Access Denied</h1>';
        return;
    }


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



    async function getRoomData() {
        try {
            const response = await fetch(`http://107.20.145.163:8003/hotel/${service_id}/people/-/room/-/minprice/1/maxprice/-`, {
                method: 'GET',
            });
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            const result = await response.json()
            console.log(result)
            provider_name.innerHTML = result.data.service_name
            providerName = result.data.service_name
            service_url = result.data.hotel_url
            console.log(service_url)
            console.log("cek")
        } catch (error) {
            console.error('Error:', error);
        }

        try {
            const urlReview = `http://3.226.141.243:8004/reviewRating/${providerName}`
            const response = await fetch(urlReview, {
                method: 'GET',
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            const result = await response.json()
            console.log(result)
            rating.innerHTML = `${result.average_rating}/5 <span
                        class="text-dark">(${result.total_reviewers})</span>`
        } catch (error) {
            console.error('Error:', error);
        }

        try {
            const url = `${service_url}/hotel/room_type/${room_id}`
            const response = await fetch(`http://52.200.174.164:8003/hotel/room_type/1`, {
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
            provider_name.innerHTML = providerName
            image_wrapper.src = result.image
            room_price_1.innerHTML = `Rp. ${formatRupiah(result.price)}`
            count.innerHTML = `(${counterValue}x)`

            updateTotalPrice()
        } catch (error) {
            console.error('Error:', error);
        }
    }
    const counterElement = document.getElementById('counter');
    const decreaseButton = document.getElementById('decrease');
    const increaseButton = document.getElementById('increase');

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
        totalPriceValue = roomPriceValue * counterValue;
        total_price.innerHTML = `Rp. ${formatRupiah(totalPriceValue)}`;
    }

    async function postBookingHotel() {
        console.log(check_in)
        console.log(check_out)
        console.log(room_id)
        const user_id = localStorage.getItem('userID');
        // console.log(user_id)
        const data = {
            user_id: user_id,
            type: "Hotel",
            total_price: totalPriceValue,
            provider_name: providerName,
            room_type: room_id,
            check_in_date: check_in,
            check_out_date: check_out,
            number_of_rooms: counterValue,
            service_id: service_id
        };
        try {
            const url = `http://3.215.46.161:8013/hotel/room_type/${check_in}&${check_out}`
            const response = await fetch(url, {
                method: 'GET'
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            var result = await response.json()
            console.log(result[0])
            console.log(room_id)
            var resultRoom = result.find(room => room.id == room_id);
            console.log(resultRoom.available_room)
            if (resultRoom.available_room >= counterValue) {
                const urlPost = `http://localhost:8000/booking`
                const response1 = await fetch(urlPost, {
                    method: 'POST',
                    body: JSON.stringify(data)
                });

                if (!response1.ok) {
                    throw new Error(`HTTP error! Status: ${response1.status}`);
                }

                const result1 = await response1.json();
                console.log(result1)
                if (result1.status == 200) {
                    const url2 = `${service_url}/hotel/reservation`
                    const data1 = {
                        booking_id: result1.booking_id,
                        check_in_date: check_in,
                        check_out_date: check_out,
                        type_id: parseInt(room_id),
                        total_room: parseInt(counterValue)
                    };
                    console.log(data1)
                    const response2 = await fetch("http://3.215.46.161:8013/hotel/reservation", {
                        method: 'POST',
                        body: JSON.stringify(data1)
                    });

                    console.log(response2.status)

                    if (!response2.ok) {
                        Swal.fire({
                            title: "Failed",
                            text: "Maaf ada kendala!",
                            icon: "error"
                        }).then((result) => {
                            // if (result.isConfirmed) {
                            //     window.location.href = `http://3.226.141.243:8004/paymentHotel.php?booking_code=${result1.booking_code}&booking_id=${result1.booking_id}`;
                            // }
                        });
                    } else {
                        Swal.fire({
                            title: "Success",
                            text: "Booking success!",
                            icon: "success"
                        }).then((result) => {
                            // if (result.isConfirmed) {
                            //     window.location.href = `http://3.226.141.243:8004/paymentHotel.php?booking_code=${result1.booking_code}&booking_id=${result1.booking_id}`;
                            // }
                        });
                    }

                }
            } else {
                Swal.fire({
                    title: "Failed",
                    text: "Room tidak tersedia!",
                    icon: "error"
                }).then((result) => {
                    // if (result.isConfirmed) {
                    //     window.location.href = `http://3.226.141.243:8004/paymentHotel.php?booking_code=${result1.booking_code}&booking_id=${result1.booking_id}`;
                    // }
                });
            }

        } catch (error) {
            console.error('Error:', error);
        }
    }

    async function coba() {
        console.log(counterValue)
        console.log(providerName)
        console.log(check_in)
        console.log(check_out)
        console.log(room_id)
        totalPriceValue = 200000
        console.log(totalPriceValue)
        // Swal.fire({
        //     title: "Success",
        //     text: "Booking success!",
        //     icon: "success"
        // })
        const data2 = {
            user_id: 1,
            type: "Hotel",
            total_price: totalPriceValue,
            provider_name: providerName,
            room_type: room_id,
            check_in_date: check_in,
            check_out_date: check_out,
            number_of_rooms: counterValue,
            service_id: service_id
        };
        try {
            const response1 = await fetch('http://localhost:8000/booking', {
                method: 'POST',
                body: JSON.stringify(data2)
            });

            if (!response1.ok) {
                throw new Error(`HTTP error! Status: ${response1.status}`);
            }
        } catch (error) {
            console.error('Error:', error);
        }

    }

    submitButton.addEventListener('click', function () {
        if (isDateInThePast(check_in) || isDateInThePast(check_out)) {
            Swal.fire({
                title: "Failed",
                text: "Invalid date!",
                icon: "error"
            })
            return
        }
        postBookingHotel()
    })
    function isDateInThePast(dateString) {
        const inputDate = new Date(dateString);

        const currentDate = new Date();

        return inputDate < currentDate;
    }
    getRoomData()

});
localStorage.setItem('userID', 1);

function formatRupiah(number) {
    return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
}
