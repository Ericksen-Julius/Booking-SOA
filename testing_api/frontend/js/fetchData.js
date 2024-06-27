let booking_id
let booking_type

async function getData() {
    const params = new URLSearchParams(window.location.search);
    const booking_code = params.get('booking_code');
    const provider = document.getElementById('provider_name');
    const total_price = document.getElementById('totalPrice');

    console.log(booking_code)
    if (!booking_code) {
        document.body.innerHTML = '<h1>Access Denied</h1>';
        return;
    }

    try {
        const response = await fetch(`http://3.226.141.243:8004/bookingDetails/${booking_code}`, {
            method: 'GET',
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        var result = await response.json();

        result = result['booking details'] // Main Booking Table
        console.log("RESULTTT", result)

        booking_id = result.id;
        booking_type = result.booking_type;
        console.log("result", booking_id);
        var url = '';
        let providerDetails = {};                // Provider Details Table
        let resultDetails = {};                  // Booking Details Table

        if (result.booking_code.charAt(0) === "H") {
            try {
                const response = await fetch(`http://3.215.46.161:8011/hotel`, {
                    method: 'GET',
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                let api_response = await response.json();
                console.log("PROVIDER", api_response);
                providerDetails['nama'] = api_response['name']
                providerDetails['alamat'] = api_response['address']
                providerDetails['kota'] = api_response['city']
                providerDetails['negara'] = api_response['country']

                if (api_response['image'] != null && typeof api_response['image'] === 'object'
                    && api_response['image']['error'] === "No AWS credentials were provided.") {
                    providerDetails['image'] = "./assets/hotel.jpeg"; // Default value
                } else {
                    providerDetails['image'] = api_response['image'] || "./assets/hotel.jpeg"; // Use API image if available, otherwise default
                }
            } catch (error) {
                console.error('Error:', error);
            }
            try {
                const response = await fetch(`http://3.215.46.161:8011/hotel/room_type/${result.room_type}`, {
                    method: 'GET',
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                resultDetails = await response.json();
                console.log("RESULTDETAIL", resultDetails);

            } catch (error) {
                console.error('Error:', error);
            }
        } else if (result.booking_code.charAt(0) == "A") {
            //Airline
            try {
                // Nanti ganti url api rental
                const response = await fetch(`http://3.228.174.120:8001/provider`, {
                    method: 'GET',
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                let api_response = await response.json();
                api_response = api_response[0];

                console.log("PROVIDER", api_response);
                providerDetails['nama'] = api_response['provider_name']
                providerDetails['alamat'] = api_response['provider_address']
                providerDetails['kota'] = api_response['provider_city']
                providerDetails['negara'] = api_response['provider_country']

                if (api_response['map'] != null && typeof api_response['map'] === 'object') {
                    providerDetails['image'] = "./assets/hotel.jpeg"; // Default value
                } else {
                    providerDetails['image'] = api_response['map'] || "./assets/hotel.jpeg"; // Use API image if available, otherwise default
                }
            } catch (error) {
                console.error('Error:', error);
            }
            try {
                const response = await fetch(`http://3.228.174.120:8001/car/${result.car_id}`, {
                    method: 'GET',
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                resultDetails = await response.json();
                console.log("resultDetails", resultDetails);

            } catch (error) {
                console.error('Error:', error);
            }
        } else if (result.booking_code.charAt(0) == "R") {
            // Rental
            try {
                // Nanti ganti url api rental
                const response = await fetch(`http://3.228.174.120:8001/provider`, {
                    method: 'GET',
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                let api_response = await response.json();
                api_response = api_response[0];

                console.log("PROVIDER", api_response);
                providerDetails['nama'] = api_response['provider_name']
                providerDetails['alamat'] = api_response['provider_address']
                providerDetails['kota'] = api_response['provider_city']
                providerDetails['negara'] = api_response['provider_country']

                if (api_response['map'] != null && typeof api_response['map'] === 'object') {
                    providerDetails['map'] = ""; // Default value
                } else {
                    providerDetails['map'] = api_response['map'] || ""; // Use API image if available, otherwise default
                }
            } catch (error) {
                console.error('Error:', error);
            }
            try {
                const response = await fetch(`http://3.228.174.120:8001/car/${result.car_id}`, {
                    method: 'GET',
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                resultDetails = await response.json();
                console.log("resultDetails", resultDetails);
                providerDetails['image'] = resultDetails['image'] || "";
            } catch (error) {
                console.error('Error:', error);
            }
        } else if (result.booking_code.charAt(0) == "T") {
            // Attraction
            try {
                // Nanti ganti url api rental
                const response = await fetch(`http://3.217.250.166:8003/api/atraksi`, {
                    method: 'GET',
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                let api_response = await response.json();
                console.log("PROVIDER", api_response);
                providerDetails['nama'] = api_response['title']
                providerDetails['alamat'] = api_response['alamat']
                providerDetails['kota'] = api_response['kota_name']
                providerDetails['negara'] = api_response['provinsi_name']

                if (api_response['photo'] != null && typeof api_response['photo'] === 'object'
                    && api_response['photo']['error'] === "No AWS credentials were provided.") {

                    providerDetails['image'] = "./assets/hotel.jpeg"; // Default value
                } else {
                    const imageUrl = api_response['photo'][0].image;
                    // Use the extracted image URL
                    providerDetails['image'] = imageUrl || "./assets/hotel.jpeg"; // Use API image if available, otherwise default
                }
            } catch (error) {
                console.error('Error:', error);
            }
            try {
                const response = await fetch(`http://3.217.250.166:8003/api/atraksi/paket/${result.paket_attraction_id}`, {
                    method: 'GET',
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                resultDetails = await response.json();
                console.log("RESULTDETAIL", resultDetails);
            } catch (error) {
                console.error('Error:', error);
            }
        } else {
            return "Error Booking code not valid", 400;
        }

        // ######################################################################################################### //

        provider.innerHTML = result.provider_name;
        total_price.innerHTML = formatCurrency(result.total_price);
        let UIType = result.booking_code.charAt(0);

        let details;
        let info = `
            <img src="./assets/hotel.jpeg" alt="" class="w-100 mb-3">
                    <div class="row mb-2">
                        <div class="col-7">
                            ${providerDetails.nama}
                        </div>
                        <div class="col-1"></div>
                        <div class="col-4 text-primary fw-bolder text-end">
                            Show Map
                        </div>
                    </div>
                    <div class="row mb-2">
                        <div class="col-12">
                            ${providerDetails.alamat}
                        </div>
                    </div>
                    <div class="row mb-2">
                        <div class="col-12">
                            ${providerDetails.kota}
                        </div>
                    </div>
                    <div class="row mb-2">
                        <div class="col-12">
                            ${providerDetails.negara}
                        </div>
                    </div>
                    <hr style="border: none; border-top: 2px solid #0d6efd;">
                    <div class="row mb-2">
                        <div class="fw-bolder col-12">
                            Got a question?
                        </div>
                    </div>
                    <div class="row mb-2">
                        <div class="col-12">
                            +62 123456789
                        </div>
                    </div>
                    <div class="row mb-2">
                        <div class="text-primary col-12">
                            Email the property
                        </div>
                    </div>
                    <hr style="border: none; border-top: 2px solid #0d6efd;">
                    <div class="row mb-2">
                        <div class="col-12">
                            &#x3F; <span class="fw-bolder">Need Help?</span>
                        </div>
                    </div>
                    <div class="row mb-2">
                        <div class="col-12 text-primary">
                            Contact customer service
                        </div>
                    </div>
                `;
        let book = `
            <div class="row mb-2">
                <div class="col-6 text-center">
                    <p class="fw-bolder mb-2">Booking code</p>
                    <p>${result.booking_code}</p>
                </div>
                <div class="col-6 text-center">
                    <p class="fw-bolder mb-2">Payment method</p>
                    <p>GoPay</p>
                </div>
            </div>`;

        let recipient = `
            <div class="col-sm-4 col-6 text-center">
                <p class="fw-bolder mb-2">Recipient name</p>
                <p>Yan Witanto</p>
            </div>
            <div class="col-sm-4 col-6 text-center">
                <p class="fw-bolder mb-2">Phone number</p>
                <p>08182738263</p>
            </div>
            <div class="col-sm-4 col-12 text-center">
                <p class="fw-bolder mb-2">Email address</p>
                <p>yan@gmail.com</p>
            </div>`;

        if (UIType === 'H') {
            details = `
                <div class="col-sm-3 col-12 m-0 mb-2">
                    <img src="${providerDetails.image}" class="w-100" alt="VIP Hotel">
                </div>
                <div class="col-sm-9 col-12">
                    <div class="row mb-2">
                        <div class="col-3">
                            <p class="fw-bolder mb-2">Room Type</p>
                            <p>${resultDetails.type}</p>
                        </div>
                        <div class="col-3">
                            <p class="fw-bolder mb-2">Night(s)</p>
                            <p>${result.number_of_nights}</p>
                        </div>
                        <div class="col-3">
                            <p class="fw-bolder mb-2">Quantity</p>
                            <p>${result.number_of_nights}</p>
                        </div>
                        <div class="col-3">
                            <p class="fw-bolder mb-2">Price</p>
                            <p>Rp. ${resultDetails.total_price}</p>
                        </div>

                    </div>
                    <div class="row mb-2">
                        <div class="col-6">
                            <p class="fw-bolder mb-2">Check-in</p>
                            <p>${convertDateToIndonesian(result.check_in_date)}</p>
                        </div>
                        <div class="col-6">
                            <p class="fw-bolder mb-2">Check-out</p>
                            <p>${convertDateToIndonesian(result.check_out_date)}</p>
                        </div>
                    </div>
                </div>`;
        } else if (UIType === 'A') {
            details = `
                <div class="col-sm-3 col-12 m-0 mb-2">
                    <img src="${providerDetails.image}" class="w-100" alt="VIP Hotel">
                </div>
                <div class="col-sm-9 col-12">
                    <div class="row mb-2">
                        <div class="col-3">
                            <p class="fw-bolder mb-2">Flight class</p>
                            <p>Economy</p>
                        </div>
                        <div class="col-3">
                            <p class="fw-bolder mb-2">Flight id</p>
                            <p>${result.flight_id}</p>
                        </div>
                        <div class="col-3">
                            <p class="fw-bolder mb-2">Quantity</p>
                            <p>1</p>
                        </div>
                        <div class="col-3">
                            <p class="fw-bolder mb-2">Price</p>
                            <p>Rp. 15,000,000</p>
                        </div>
                    </div>
                    <div class="row mb-2">
                        <div class="col-6">
                            <p class="fw-bolder mb-2">Departure time</p>
                            <p>Sat, June 1 2024 10:00 PM</p>
                        </div>
                        <div class="col-6">
                            <p class="fw-bolder mb-2">Arrival time</p>
                            <p>Sat, June 3 2024 12:00 PM</p>
                        </div>
                    </div>
                    <div class="row mb-2">
                        <div class="col-6">
                            <p class="fw-bolder mb-2">From</p>
                            <p>Surabaya</p>
                        </div>
                        <div class="col-6">
                            <p class="fw-bolder mb-2">To</p>
                            <p>Jakarta</p>
                        </div>
                    </div>
                </div>`;
        } else if (UIType === 'R') {
            details = `
                <div class="col-sm-3 col-12 m-0 mb-2">
                    <img src="${providerDetails.image}" class="w-100" alt="VIP Hotel">
                </div>
                <div class="col-sm-9 col-12">
                    <div class="row mb-2">
                        <div class="col-3">
                            <p class="fw-bolder mb-2">Car</p>
                            <p>${resultDetails.car_brand} ${resultDetails.car_name}</p>
                        </div>
                        <div class="col-3">
                            <p class="fw-bolder mb-2">Day(s)</p>
                            <p>${calculateDays(result.pickupDate, result.returnDate)} Days</p>
                        </div>
                        <div class="col-3">
                            <p class="fw-bolder mb-2">Is With Driver</p>
                            <p>${result.is_with_driver == true ? 'Yes' : 'No'}</p>
                        </div>
                        <div class="col-3">
                            <p class="fw-bolder mb-2">Price</p>
                            <p>Rp. ${resultDetails.car_price}/Day</p>
                        </div>
                    </div>
                    <div class="row mb-2">
                        <div class="col-6">
                            <p class="fw-bolder mb-2">Pick Up Date</p>
                            <p>${convertDateToIndonesian(result.pickup_date)}</p>
                        </div>
                        <div class="col-6">
                            <p class="fw-bolder mb-2">Return Date</p>
                            <p>${convertDateToIndonesian(result.return_date)}</p>
                        </div>
                    </div>
                    <div class="row mb-2">
                        <div class="col-6">
                            <p class="fw-bolder mb-2">Pick Up Location</p>
                            <p>${result.pickup_location}</p>
                        </div>
                        <div class="col-6">
                            <p class="fw-bolder mb-2">Return Location</p>
                            <p>${result.return_location}</p>
                        </div>
                    </div>
                </div>`;
        } else if (UIType === 'T') {
            details = `
                <div class="col-sm-3 col-12 m-0 mb-2">
                    <img src="${providerDetails.image}" class="w-100" alt="VIP Hotel">
                </div>
                <div class="col-sm-9 col-12">
                    <div class="row mb-2">
                        <div class="col-4">
                            <p class="fw-bolder mb-2">Type</p>
                            <p>${result.paket_attraction_id}</p>
                        </div>
                        <div class="col-4">
                            <p class="fw-bolder mb-2">Quantity</p>
                            <p>1</p>
                        </div>
                        <div class="col-4">
                            <p class="fw-bolder mb-2">Price</p>
                            <p>Rp. 15,000,000</p>
                        </div>
                    </div>
                    <div class="row mb-2">
                        <div class="col-6">
                            <p class="fw-bolder mb-2">E-ticket number</p>
                            <p>#345</p>
                        </div>
                        <div class="col-6">
                            <p class="fw-bolder mb-2">Visit date</p>
                            <p>${result.visit_date}</p>
                        </div>
                    </div>
                </div>`;
        }
        document.getElementById('detailContainer').innerHTML = details;
        document.getElementById('infoContainer').innerHTML = info;
        document.getElementById('bookContainer').innerHTML = book;
        document.getElementById('recipientContainer').innerHTML = recipient;
        getReview(booking_type);
    } catch (error) {
        console.error('Error:', error);
    }


}

<<<<<<< HEAD
async function getReview(booking_id, booking_type) {
=======
async function getReview(booking_type){
>>>>>>> b4777528f4329a0c9a09d95c7b2041be9c70a81d
    try {
        const response = await fetch(`http://localhost:8000/get_review_options/${booking_type}`, {
            method: 'GET',
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const reviewButton = document.getElementById('review')
        const result = await response.json();
        console.log(result)
        if (result.length === 0) {
            reviewButton.innerHTML = "Write a Review";
        } else {
            reviewButton.innerHTML = "Edit Review";
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

async function postReview(booking_id, rating, comment) {
    try {
        const data = {
            booking_id: booking_id,
            rating: rating,
            comment: comment,
            option_id: []
        };
        const response = await fetch(`http://3.226.141.243:8004/review`, {
            method: 'POST',
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const result = await response.json();
        if (result.message == "Review added successfully") {
            Swal.fire({
                title: "Success",
                text: "Berhasil memberikan review!",
                icon: "success"
            }).then((result) => {
                if (result.isConfirmed) {
                    location.reload();
                }
            });
        }
    } catch (error) {
        console.error('Error:', error);
    }

}

async function getReviewDate(booking_id, booking_type) {
    try {
        const response = await fetch(`http://3.226.141.243:8004/getDate/${booking_id}/${booking_type}`, {
            method: 'GET'
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const result = await response.json();
        console.log(result)
        const reviewButton = document.getElementById('review')
        if (result.data.reviewed) {
            reviewButton.style.display = 'none'
        } else if (isDatePassed(result.data.date) == false) {
            reviewButton.style.display = 'none'
        } else {
            reviewButton.style.display = 'inline'
        }
    } catch (error) {
        console.log(error)
    }
}

function isDatePassed(targetDateStr) {
    const currentDate = new Date();

    const targetDate = new Date(targetDateStr);

    return currentDate > targetDate;
}



function formatCurrency(amount) {
    return new Intl.NumberFormat('id-ID', { style: 'currency', currency: 'IDR' }).format(amount);
}

function convertDateToIndonesian(dateStr) {
    const months = [
        'Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni',
        'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'
    ];

    const [year, monthIndex, day] = dateStr.split('-');

    const monthName = months[parseInt(monthIndex, 10) - 1];

    const formattedDate = `${parseInt(day, 10)} ${monthName} ${year}`;

    return formattedDate;
}
function calculateDays(startDateStr, endDateStr) {
    // Parse the input date strings into Date objects
    let startDate = new Date(startDateStr);
    let endDate = new Date(endDateStr);

    // Calculate the difference in milliseconds
    let timeDifference = endDate.getTime() - startDate.getTime();

    // Convert milliseconds to days
    let daysDifference = timeDifference / (1000 * 3600 * 24);

    // Round down to get the whole number of days
    daysDifference = Math.floor(daysDifference);

    return daysDifference;
}

document.addEventListener('DOMContentLoaded', (event) => {
    getData();
    getReviewDate(booking_id, booking_type)
    const reviewButton = document.getElementById('review');
    reviewButton.style.display = 'none'
    const modal = document.getElementById('reviewModal');
    let valueStar = 0
    const comment = document.getElementById('comment');
    const buttonSubmit = document.getElementById('submitComment');
    const stars = modal.querySelectorAll('.rating-stars i');
    stars.forEach(star => {
        star.addEventListener('click', () => {
            const value = parseInt(star.getAttribute('data-value'));
            stars.forEach(s => s.classList.remove('active'));
            for (let i = 0; i < value; i++) {
                stars[i].classList.add('active');
            }
            // document.querySelector('.rating input').value = value;
            valueStar = value;
            console.log(valueStar)
        });
    });
    buttonSubmit.addEventListener('click', () => {
        console.log(comment.value)
    })
    // getReviewDate(84, 'Hotel')



});
