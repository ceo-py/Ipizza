(function ($) {
    "use strict";

    // Initiate superfish on nav menu
    $('.nav-menu').superfish({
        animation: {opacity: 'show'},
        speed: 400
    });

    // Mobile Navigation
    if ($('#nav-menu-container').length) {
        var $mobile_nav = $('#nav-menu-container').clone().prop({id: 'mobile-nav'});
        $mobile_nav.find('> ul').attr({'class': '', 'id': ''});
        $('body').append($mobile_nav);
        $('body').prepend('<button type="button" id="mobile-nav-toggle"><i class="fa fa-bars"></i></button>');
        $('body').append('<div id="mobile-body-overly"></div>');
        $('#mobile-nav').find('.menu-has-children').prepend('<i class="fa fa-chevron-down"></i>');

        $(document).on('click', '.menu-has-children i', function (e) {
            $(this).next().toggleClass('menu-item-active');
            $(this).nextAll('ul').eq(0).slideToggle();
            $(this).toggleClass("fa-chevron-up fa-chevron-down");
        });

        $(document).on('click', '#mobile-nav-toggle', function (e) {
            $('body').toggleClass('mobile-nav-active');
            $('#mobile-nav-toggle i').toggleClass('fa-times fa-bars');
            $('#mobile-body-overly').toggle();
        });

        $(document).click(function (e) {
            var container = $("#mobile-nav, #mobile-nav-toggle");
            if (!container.is(e.target) && container.has(e.target).length === 0) {
                if ($('body').hasClass('mobile-nav-active')) {
                    $('body').removeClass('mobile-nav-active');
                    $('#mobile-nav-toggle i').toggleClass('fa-times fa-bars');
                    $('#mobile-body-overly').fadeOut();
                }
            }
        });
    } else if ($("#mobile-nav, #mobile-nav-toggle").length) {
        $("#mobile-nav, #mobile-nav-toggle").hide();
    }

    // Stick the header at top on scroll
    $("#header").sticky({topSpacing: 0, zIndex: '50'});

    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });

    // Header scroll class
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('#header').addClass('header-scrolled');
        } else {
            $('#header').removeClass('header-scrolled');
        }
    });

    if ($(window).scrollTop() > 100) {
        $('#header').addClass('header-scrolled');
    }

    // Testimonials carousel (uses the Owl Carousel library)
    $(".testimonials-carousel").owlCarousel({
        autoplay: true,
        dots: true,
        loop: true,
        items: 1
    });

    // + - button on cart and total logic here
    function calculateTotalCard() {
        var body = $('body')
        var totalCart = body.find('.product-card span');
        var shipment = parseFloat(body.find('.shipment span').text().split(' лв.')[0]);
        var totalPayment = body.find('.total-card span');
        var totalPrice = body.find('.total-price')
        var sumAll = totalPrice.text()
            .slice(0, -1)
            .split(' лв.')
            .reduce((accumulator, currentValue) => accumulator + parseFloat(currentValue), 0);
        totalCart.text(isNaN(sumAll) ? '0 лв.' : sumAll.toFixed(2) + ' лв.');
        totalPayment.text(isNaN(sumAll) ? '0 лв.' : (sumAll + shipment).toFixed(2) + ' лв.');
    }


    // + - buttons logic
    $('.q-btn').on('click', function () {
        var $button = $(this);
        var singlePrice = parseFloat($button.closest('tr').find('.single-price').text());
        var $totalPrice = $button.closest('tr').find('.total-price');
        var oldValue = $button.parent().find('input').val();
        if ($button.hasClass('btn-add-cart')) {
            addToCartIcon($button)
        }

        if ($button.hasClass('inc')) {
            var newVal = parseFloat(oldValue) + 1;
        } else {
            if (oldValue > 0) {
                var newVal = parseFloat(oldValue) - 1;
            } else {
                newVal = 0;
            }
        }
        $button.parent().find('input').val(newVal);
        if (singlePrice) {
            var totalItem = (newVal * singlePrice).toFixed(2);
            $totalPrice.text(totalItem + ' лв.');
            calculateTotalCard()

        } else {
            var htmlPrice = $button.parent().parent().find('.price-total');
            var price = $button.parent().find('input').attr('price')
            htmlPrice.text((price * newVal).toFixed(2) + ' лв.')
        }
    });

    //menu color
    const activeMenu = localStorage.getItem('activeMenu');
    if (activeMenu) {
        $('.nav-menu li a[data-menu="' + activeMenu + '"]').parent().addClass('menu-active');
    }

    // Handle menu clicks
    $('.nav-menu li a').on('click', function () {
        const menu = $(this).data('menu');
        // Add "menu-active" class to the clicked menu item
        $(this).parent().addClass('menu-active');
        // Remove "menu-active" class from other menu items
        $('.nav-menu li a').not(this).parent().removeClass('menu-active');
        // Store the active menu item in local storage
        localStorage.setItem('activeMenu', menu);
    });

    //handle cart remove btn
    $('.delete-btn').on('click', function () {
            // Go up two parent elements to reach the 'td' element
            var $tdElement = $(this).closest('td').closest('td');
            var itemName = $(this).data();
            // Remove the 'tr' (table row) element
            $tdElement.parent().remove();
            calculateTotalCard();
            apiDeleteCart(itemName);

        }
    )

    //handle add to cart button from the menu
    $('.order-link').on('click', function (event) {
            event.preventDefault()
            if ($('body').find('.menu-has-children').length === 0) {

                window.location.href = "/login";
                return
            }
            const singleMenu = $(this).closest('.single-menu');

            const typeN = singleMenu.find('input');
            const dataJson = {
                'item_name': singleMenu.find('h4').text(),
                'quantity': typeN.val(),
                'picture': singleMenu.find('.img-fluid').attr('src').substring(7),
                'price': typeN.attr('price'),
            }
            const menu = singleMenu.find('.menu');
            menu.toggleClass('hidden');
            // description.toggleClass('hidden')
            if (menu.hasClass('hidden')) {
                addToCartIcon($(this))
                $(this).text('Поръчай')
                apiRequest('/api/add/', 'POST', dataJson)
                // apiRequest('/api/delete/', 'DELETE', dataJson)
            } else {
                $(this).text('Добави')
            }
            // $(this).text(menu.hasClass('hidden') ? 'Поръчай' : 'Добави');
        }
    )

    // add to card icon from buttons
    function addToCartIcon(button) {
        const addedItems = parseInt(button.parent().find('input').val());
        const totalItemsCart = $('body').find('.icon-header-noti');
        const currentItems = parseInt(totalItemsCart.attr('data-notify'));
        totalItemsCart.attr('data-notify', isNaN(currentItems) ? addedItems : currentItems + addedItems);
    }

    // getting csrf from co
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === name + '=') {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // cart remove btn remove from db item also
    function apiDeleteCart(item_name) {
        const dataJson = {
            'item_name': item_name,
        }
        apiRequest('/api/delete/', 'DELETE', dataJson)
    }

    // api request
    function apiRequest(url, methodType, data) {
        const csrfToken = getCookie('csrftoken');
        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader('X-CSRFToken', csrfToken);
                }
            }
        });
        $.ajax({
            url: url,
            type: methodType,
            data: data,
            dataType: 'json',
            headers: {
                'Authorization': `Token ${csrfToken}`,
            }
        });
    }


    // add data to cart on add to click
    $('.btn-add-cart').on('click', function () {
        const button = $(this);
        const item_name = button.data('name');
        const price = button.data('price');
        const picture = button.data('image');
        const quantity = button.closest('tr').find('input[type="number"]').val();
        const csrfToken = getCookie('csrftoken');
        // console.log(csrfToken)
        // console.log(item_name)
        // console.log(price)
        // console.log(quantity)
        // console.log(picture)
        const dataJson = {
            'item_name': item_name,
            'quantity': quantity,
            'picture': picture,
            'price': price,
        }
        apiRequest('/api/add/', 'POST', dataJson)
    })


    // Cart header show/hide
    $('.js-show-cart').on('click', function () {
        $('.js-panel-cart').addClass('show-header-cart');
    });

    $('.js-hide-cart').on('click', function () {
        $('.js-panel-cart').removeClass('show-header-cart');
    });

    // Cart sidebar show/hide
    $('.js-show-sidebar').on('click', function () {
        $('.js-sidebar').addClass('show-sidebar');
    });

    $('.js-hide-sidebar').on('click', function () {
        $('.js-sidebar').removeClass('show-sidebar');
    });


})(jQuery);

