(function ($) {

	'use strict';

	
	const darkBtn = document.querySelector('.fa-moon-o');
	const bodyEl = document.querySelector('body');

	const darkMode = () => {
		bodyEl.classList.toggle( 'dark' )
	}

	darkBtn.addEventListener( 'click', () => {
		// Get the value of the "dark" item from the local storage on every click
		setDarkMode = localStorage.getItem( 'dark' );

		if ( setDarkMode !== "on" ) {
			darkMode();
			// Set the value of the itwm to "on" when dark mode is on
			setDarkMode = localStorage.setItem( 'dark', 'on' );
		} else {
			darkMode();
			// Set the value of the item to  "null" when dark mode if off
			setDarkMode = localStorage.setItem( 'dark', null );
		}
	} );

	// Get the value of the "dark" item from the local storage
	let setDarkMode = localStorage.getItem( 'dark' );

	// Check dark mode is on or off on page reload
	if ( setDarkMode === 'on' ) {
		darkMode();
	}
	
	var countDownDate = new Date("April 15, 2020 00:00:00").getTime();

	var x = setInterval(function () {
		var now = new Date().getTime();
		var distance = countDownDate - now;
		var days = Math.floor(distance / (1000 * 60 * 60 * 24));
		var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
		var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
		var seconds = Math.floor((distance % (1000 * 60)) / 1000);

		$("#days .number").text(days);
		$("#hours .number").text(hours);
		$("#minutes .number").text(minutes);
		$("#seconds .number").text(seconds);
	}, 1000);

	$('.team-slider').slick({
		slidesToShow: 3,
		slidesToScroll: 1,
		autoplaySpeed: 2000,
		responsive: [{
				breakpoint: 991,
				settings: {
					slidesToShow: 2
				}
			},
			{
				breakpoint: 550,
				settings: {
					slidesToShow: 1
				}
			}
		]
	});

	$('.customer-logos').slick({
		slidesToShow: 6,
		slidesToScroll: 1,
		autoplay: true,
		autoplaySpeed: 500,
		arrows: false,
		dots: false,
		pauseOnHover: false,
		responsive: [{
			breakpoint: 768,
			settings: {
				slidesToShow: 4
			}
		}, {
			breakpoint: 520,
			settings: {
				slidesToShow: 3
			}
		}]
	});

	new WOW().init();

	let Typer = function (element) {
		this.element = element;
		let delim = element.dataset.delim || ",";
		let words = element.dataset.words || "sample sample,sample sample";
		this.words = words.split(delim).filter((v) => v);
		this.delay = element.dataset.delay || 200;
		this.loop = element.dataset.loop || "true";
		if (this.loop === "false") {
			this.loop = 1
		}
		this.deleteDelay = element.dataset.deletedelay || element.dataset.deleteDelay || 800;
		this.progress = {
			word: 0,
			char: 0,
			building: true,
			looped: 0
		};
		this.typing = true;
		let colors = element.dataset.colors || "black";
		this.colors = colors.split(",");
		this.element.style.color = this.colors[0];
		this.colorIndex = 0;
		this.doTyping();
	};

	Typer.prototype.start = function () {
		if (!this.typing) {
			this.typing = true;
			this.doTyping();
		}
	};

	Typer.prototype.stop = function () {
		this.typing = false;
	};

	Typer.prototype.doTyping = function () {
		let e = this.element;
		let p = this.progress;
		let w = p.word;
		let c = p.char;
		let currentDisplay = [...this.words[w]].slice(0, c).join("");
		let atWordEnd;
		if (this.cursor) {
			this.cursor.element.style.opacity = "1";
			this.cursor.on = true;
			clearInterval(this.cursor.interval);
			this.cursor.interval = setInterval(() => this.cursor.updateBlinkState(), 400);
		}

		e.innerHTML = currentDisplay;

		if (p.building) {
			atWordEnd = p.char === this.words[w].length;
			if (atWordEnd) {
				p.building = false;
			} else {
				p.char += 1;
			}
		} else {
			if (p.char === 0) {
				p.building = true;
				p.word = (p.word + 1) % this.words.length;
				this.colorIndex = (this.colorIndex + 1) % this.colors.length;
				this.element.style.color = this.colors[this.colorIndex];
			} else {
				p.char -= 1;
			}
		}

		if (p.word === this.words.length - 1) {
			p.looped += 1;
		}

		if (!p.building && this.loop <= p.looped) {
			this.typing = false;
		}

		setTimeout(() => {
			if (this.typing) {
				this.doTyping()
			};
		}, atWordEnd ? this.deleteDelay : this.delay);
	};

	let Cursor = function (element) {
		this.element = element;
		this.cursorDisplay = element.dataset.cursordisplay || element.dataset.cursorDisplay || "_";
		element.innerHTML = this.cursorDisplay;
		this.on = true;
		element.style.transition = "all 0.1s";
		this.interval = setInterval(() => this.updateBlinkState(), 400);
	}

	Cursor.prototype.updateBlinkState = function () {
		if (this.on) {
			this.element.style.opacity = "0";
			this.on = false;
		} else {
			this.element.style.opacity = "1";
			this.on = true;
		}
	}

	function TyperSetup() {
		let typers = {};
		for (let e of document.getElementsByClassName("typer")) {
			typers[e.id] = new Typer(e);
		}
		for (let e of document.getElementsByClassName("typer-stop")) {
			let owner = typers[e.dataset.owner];
			e.onclick = () => owner.stop();
		}
		for (let e of document.getElementsByClassName("typer-start")) {
			let owner = typers[e.dataset.owner];
			e.onclick = () => owner.start();
		}
		for (let e of document.getElementsByClassName("cursor")) {
			let t = new Cursor(e);
			t.owner = typers[e.dataset.owner];
			t.owner.cursor = t;
		}
	}

	TyperSetup();

	const nodes = Array.from(document.getElementsByClassName("time-title"));
	const cache = {
		viewport: {},
		rects: []
	};

	window.addEventListener("load", init);

	function init() {
		recache();
		document.addEventListener("scroll", throttle(scrollCheck, 10));
		window.addEventListener("resize", debounce(recache, 50));
	};

	function recache() {
		cache.viewport = {
			width: window.innerWidth,
			height: window.innerHeight
		};
		nodes.forEach((node, i) => {
			cache.rects[i] = rect(node);
		});

		scrollCheck();
	}

	function scrollCheck() {
		const offset = getScrollOffset();
		const midline = cache.viewport.height * 0.3;
		cache.rects.forEach((rect, i) => {
			nodes[i].classList.toggle("active", rect.y - offset.y < midline);
		});
	};

	function getScrollOffset() {
		return {
			x: window.pageXOffset,
			y: window.pageYOffset
		};
	};

	function throttle(fn, limit, context) {
		let wait;
		return function () {
			context = context || this;
			if (!wait) {
				fn.apply(context, arguments);
				wait = true;
				return setTimeout(function () {
					wait = false;
				}, limit);
			}
		};
	};

	function debounce(fn, limit, u) {
		let e;
		return function () {
			const i = this;
			const o = arguments;
			const a = u && !e;
			clearTimeout(e),
				(e = setTimeout(function () {
					(e = null), u || fn.apply(i, o);
				}, limit)),
				a && fn.apply(i, o);
		};

	}

	function rect(e) {
		const o = getScrollOffset();
		const r = e.getBoundingClientRect();

		return {
			x: r.left + o.x,
			y: r.top + o.y
		};
	};

	$('.counter_num').each(function () {
		$(this).prop('Counter', 0).animate({
			Counter: $(this).text()
		}, {
			duration: 4000,
			easing: 'swing',
			step: function (now) {
				$(this).text(Math.ceil(now));
			}
		});
	});

})(jQuery);

// Fancybox
$(document).ready(function () {
	$('.fancybox').fancybox({
		padding: 0,
		maxWidth: '100%',
		maxHeight: '100%',
		width: 560,
		height: 315,
		autoSize: true,
		closeClick: true,
		openEffect: 'elastic',
		closeEffect: 'elastic'
	});
});

// Smooth Scroll to Top
$(document).ready(function () {
	var offset = 220;
	var duration = 500;
	$(window).scroll(function () {
		if ($(this).scrollTop() > offset) {
			$('.scroll-top').fadeIn(duration);
		} else {
			$('.scroll-top').fadeOut(duration);
		}
	});
	$('.scroll-top').click(function (event) {
		event.preventDefault();
		$('html, body').animate({
			scrollTop: 0
		}, duration);
		return false;
	})
});
$(document).ready(function () {
	$(".fancybox").fancybox({
		padding: 0,
		maxWidth: "100%",
		maxHeight: "100%",
		width: 560,
		height: 315,
		autoSize: !0,
		closeClick: !0,
		openEffect: "elastic",
		closeEffect: "elastic"
	})
}), $(document).ready(function () {
	var o = 220,
		t = 500;
	$(window).scroll(function () {
		$(this).scrollTop() > o ? $(".scroll-top").fadeIn(t) : $(".scroll-top").fadeOut(t)
	}), $(".scroll-top").click(function (o) {
		return o.preventDefault(), $("html, body").animate({
			scrollTop: 0
		}, t), !1
	})
});
/*!
 * fancyBox - jQuery Plugin
 * version: 2.1.5 (Fri, 14 Jun 2013)
 * requires jQuery v1.6 or later
 *
 * Examples at http://fancyapps.com/fancybox/
 * License: www.fancyapps.com/fancybox/#license
 *
 * Copyright 2012 Janis Skarnelis - janis@fancyapps.com
 *
 */

;
(function (window, document, $, undefined) {
	"use strict";

	var H = $("html"),
		W = $(window),
		D = $(document),
		F = $.fancybox = function () {
			F.open.apply(this, arguments);
		},
		IE = navigator.userAgent.match(/msie/i),
		didUpdate = null,
		isTouch = document.createTouch !== undefined,

		isQuery = function (obj) {
			return obj && obj.hasOwnProperty && obj instanceof $;
		},
		isString = function (str) {
			return str && $.type(str) === "string";
		},
		isPercentage = function (str) {
			return isString(str) && str.indexOf('%') > 0;
		},
		isScrollable = function (el) {
			return (el && !(el.style.overflow && el.style.overflow === 'hidden') && ((el.clientWidth && el.scrollWidth > el.clientWidth) || (el.clientHeight && el.scrollHeight > el.clientHeight)));
		},
		getScalar = function (orig, dim) {
			var value = parseInt(orig, 10) || 0;

			if (dim && isPercentage(orig)) {
				value = F.getViewport()[dim] / 100 * value;
			}

			return Math.ceil(value);
		},
		getValue = function (value, dim) {
			return getScalar(value, dim) + 'px';
		};

	$.extend(F, {
		// The current version of fancyBox
		version: '2.1.5',

		defaults: {
			padding: 15,
			margin: 20,

			width: 800,
			height: 600,
			minWidth: 100,
			minHeight: 100,
			maxWidth: 9999,
			maxHeight: 9999,
			pixelRatio: 1, // Set to 2 for retina display support

			autoSize: true,
			autoHeight: false,
			autoWidth: false,

			autoResize: true,
			autoCenter: !isTouch,
			fitToView: true,
			aspectRatio: false,
			topRatio: 0.5,
			leftRatio: 0.5,

			scrolling: 'auto', // 'auto', 'yes' or 'no'
			wrapCSS: '',

			arrows: true,
			closeBtn: true,
			closeClick: false,
			nextClick: false,
			mouseWheel: true,
			autoPlay: false,
			playSpeed: 3000,
			preload: 3,
			modal: false,
			loop: true,

			ajax: {
				dataType: 'html',
				headers: {
					'X-fancyBox': true
				}
			},
			iframe: {
				scrolling: 'no',
				preload: true
			},
			swf: {
				wmode: 'transparent',
				allowfullscreen: 'true',
				allowscriptaccess: 'always'
			},

			keys: {
				next: {
					13: 'left', // enter
					34: 'up', // page down
					39: 'left', // right arrow
					40: 'up' // down arrow
				},
				prev: {
					8: 'right', // backspace
					33: 'down', // page up
					37: 'right', // left arrow
					38: 'down' // up arrow
				},
				close: [27], // escape key
				play: [32], // space - start/stop slideshow
				toggle: [70] // letter "f" - toggle fullscreen
			},

			direction: {
				next: 'left',
				prev: 'right'
			},

			scrollOutside: true,

			// Override some properties
			index: 0,
			type: null,
			href: null,
			content: null,
			title: null,

			// HTML templates
			tpl: {
				wrap: '<div class="fancybox-wrap" tabIndex="-1"><div class="fancybox-skin"><div class="fancybox-outer"><div class="fancybox-inner"></div></div></div></div>',
				image: '<img class="fancybox-image" src="{href}" alt="" />',
				iframe: '<iframe id="fancybox-frame{rnd}" name="fancybox-frame{rnd}" class="fancybox-iframe" frameborder="0" vspace="0" hspace="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen' + (IE ? ' allowtransparency="true"' : '') + '></iframe>',
				error: '<p class="fancybox-error">The requested content cannot be loaded.<br/>Please try again later.</p>',
				closeBtn: '<a title="Close" class="fancybox-item fancybox-close" href="javascript:;"></a>',
				next: '<a title="Next" class="fancybox-nav fancybox-next" href="javascript:;"><span></span></a>',
				prev: '<a title="Previous" class="fancybox-nav fancybox-prev" href="javascript:;"><span></span></a>'
			},

			// Properties for each animation type
			// Opening fancyBox
			openEffect: 'fade', // 'elastic', 'fade' or 'none'
			openSpeed: 250,
			openEasing: 'swing',
			openOpacity: true,
			openMethod: 'zoomIn',

			// Closing fancyBox
			closeEffect: 'fade', // 'elastic', 'fade' or 'none'
			closeSpeed: 250,
			closeEasing: 'swing',
			closeOpacity: true,
			closeMethod: 'zoomOut',

			// Changing next gallery item
			nextEffect: 'elastic', // 'elastic', 'fade' or 'none'
			nextSpeed: 250,
			nextEasing: 'swing',
			nextMethod: 'changeIn',

			// Changing previous gallery item
			prevEffect: 'elastic', // 'elastic', 'fade' or 'none'
			prevSpeed: 250,
			prevEasing: 'swing',
			prevMethod: 'changeOut',

			// Enable default helpers
			helpers: {
				overlay: true,
				title: true
			},

			// Callbacks
			onCancel: $.noop, // If canceling
			beforeLoad: $.noop, // Before loading
			afterLoad: $.noop, // After loading
			beforeShow: $.noop, // Before changing in current item
			afterShow: $.noop, // After opening
			beforeChange: $.noop, // Before changing gallery item
			beforeClose: $.noop, // Before closing
			afterClose: $.noop // After closing
		},

		//Current state
		group: {}, // Selected group
		opts: {}, // Group options
		previous: null, // Previous element
		coming: null, // Element being loaded
		current: null, // Currently loaded element
		isActive: false, // Is activated
		isOpen: false, // Is currently open
		isOpened: false, // Have been fully opened at least once

		wrap: null,
		skin: null,
		outer: null,
		inner: null,

		player: {
			timer: null,
			isActive: false
		},

		// Loaders
		ajaxLoad: null,
		imgPreload: null,

		// Some collections
		transitions: {},
		helpers: {},

		/*
		 *	Static methods
		 */

		open: function (group, opts) {
			if (!group) {
				return;
			}

			if (!$.isPlainObject(opts)) {
				opts = {};
			}

			// Close if already active
			if (false === F.close(true)) {
				return;
			}

			// Normalize group
			if (!$.isArray(group)) {
				group = isQuery(group) ? $(group).get() : [group];
			}

			// Recheck if the type of each element is `object` and set content type (image, ajax, etc)
			$.each(group, function (i, element) {
				var obj = {},
					href,
					title,
					content,
					type,
					rez,
					hrefParts,
					selector;

				if ($.type(element) === "object") {
					// Check if is DOM element
					if (element.nodeType) {
						element = $(element);
					}

					if (isQuery(element)) {
						obj = {
							href: element.data('fancybox-href') || element.attr('href'),
							title: element.data('fancybox-title') || element.attr('title'),
							isDom: true,
							element: element
						};

						if ($.metadata) {
							$.extend(true, obj, element.metadata());
						}

					} else {
						obj = element;
					}
				}

				href = opts.href || obj.href || (isString(element) ? element : null);
				title = opts.title !== undefined ? opts.title : obj.title || '';

				content = opts.content || obj.content;
				type = content ? 'html' : (opts.type || obj.type);

				if (!type && obj.isDom) {
					type = element.data('fancybox-type');

					if (!type) {
						rez = element.prop('class').match(/fancybox\.(\w+)/);
						type = rez ? rez[1] : null;
					}
				}

				if (isString(href)) {
					// Try to guess the content type
					if (!type) {
						if (F.isImage(href)) {
							type = 'image';

						} else if (F.isSWF(href)) {
							type = 'swf';

						} else if (href.charAt(0) === '#') {
							type = 'inline';

						} else if (isString(element)) {
							type = 'html';
							content = element;
						}
					}

					// Split url into two pieces with source url and content selector, e.g,
					// "/mypage.html #my_id" will load "/mypage.html" and display element having id "my_id"
					if (type === 'ajax') {
						hrefParts = href.split(/\s+/, 2);
						href = hrefParts.shift();
						selector = hrefParts.shift();
					}
				}

				if (!content) {
					if (type === 'inline') {
						if (href) {
							content = $(isString(href) ? href.replace(/.*(?=#[^\s]+$)/, '') : href); //strip for ie7

						} else if (obj.isDom) {
							content = element;
						}

					} else if (type === 'html') {
						content = href;

					} else if (!type && !href && obj.isDom) {
						type = 'inline';
						content = element;
					}
				}

				$.extend(obj, {
					href: href,
					type: type,
					content: content,
					title: title,
					selector: selector
				});

				group[i] = obj;
			});

			// Extend the defaults
			F.opts = $.extend(true, {}, F.defaults, opts);

			// All options are merged recursive except keys
			if (opts.keys !== undefined) {
				F.opts.keys = opts.keys ? $.extend({}, F.defaults.keys, opts.keys) : false;
			}

			F.group = group;

			return F._start(F.opts.index);
		},

		// Cancel image loading or abort ajax request
		cancel: function () {
			var coming = F.coming;

			if (false === F.trigger('onCancel')) {
				return;
			}

			F.hideLoading();

			if (!coming) {
				return;
			}

			if (F.ajaxLoad) {
				F.ajaxLoad.abort();
			}

			F.ajaxLoad = null;

			if (F.imgPreload) {
				F.imgPreload.onload = F.imgPreload.onerror = null;
			}

			if (coming.wrap) {
				coming.wrap.stop(true, true).trigger('onReset').remove();
			}

			F.coming = null;

			// If the first item has been canceled, then clear everything
			if (!F.current) {
				F._afterZoomOut(coming);
			}
		},

		// Start closing animation if is open; remove immediately if opening/closing
		close: function (event) {
			F.cancel();

			if (false === F.trigger('beforeClose')) {
				return;
			}

			F.unbindEvents();

			if (!F.isActive) {
				return;
			}

			if (!F.isOpen || event === true) {
				$('.fancybox-wrap').stop(true).trigger('onReset').remove();

				F._afterZoomOut();

			} else {
				F.isOpen = F.isOpened = false;
				F.isClosing = true;

				$('.fancybox-item, .fancybox-nav').remove();

				F.wrap.stop(true, true).removeClass('fancybox-opened');

				F.transitions[F.current.closeMethod]();
			}
		},

		// Manage slideshow:
		//   $.fancybox.play(); - toggle slideshow
		//   $.fancybox.play( true ); - start
		//   $.fancybox.play( false ); - stop
		play: function (action) {
			var clear = function () {
					clearTimeout(F.player.timer);
				},
				set = function () {
					clear();

					if (F.current && F.player.isActive) {
						F.player.timer = setTimeout(F.next, F.current.playSpeed);
					}
				},
				stop = function () {
					clear();

					D.unbind('.player');

					F.player.isActive = false;

					F.trigger('onPlayEnd');
				},
				start = function () {
					if (F.current && (F.current.loop || F.current.index < F.group.length - 1)) {
						F.player.isActive = true;

						D.bind({
							'onCancel.player beforeClose.player': stop,
							'onUpdate.player': set,
							'beforeLoad.player': clear
						});

						set();

						F.trigger('onPlayStart');
					}
				};

			if (action === true || (!F.player.isActive && action !== false)) {
				start();
			} else {
				stop();
			}
		},

		// Navigate to next gallery item
		next: function (direction) {
			var current = F.current;

			if (current) {
				if (!isString(direction)) {
					direction = current.direction.next;
				}

				F.jumpto(current.index + 1, direction, 'next');
			}
		},

		// Navigate to previous gallery item
		prev: function (direction) {
			var current = F.current;

			if (current) {
				if (!isString(direction)) {
					direction = current.direction.prev;
				}

				F.jumpto(current.index - 1, direction, 'prev');
			}
		},

		// Navigate to gallery item by index
		jumpto: function (index, direction, router) {
			var current = F.current;

			if (!current) {
				return;
			}

			index = getScalar(index);

			F.direction = direction || current.direction[(index >= current.index ? 'next' : 'prev')];
			F.router = router || 'jumpto';

			if (current.loop) {
				if (index < 0) {
					index = current.group.length + (index % current.group.length);
				}

				index = index % current.group.length;
			}

			if (current.group[index] !== undefined) {
				F.cancel();

				F._start(index);
			}
		},

		// Center inside viewport and toggle position type to fixed or absolute if needed
		reposition: function (e, onlyAbsolute) {
			var current = F.current,
				wrap = current ? current.wrap : null,
				pos;

			if (wrap) {
				pos = F._getPosition(onlyAbsolute);

				if (e && e.type === 'scroll') {
					delete pos.position;

					wrap.stop(true, true).animate(pos, 200);

				} else {
					wrap.css(pos);

					current.pos = $.extend({}, current.dim, pos);
				}
			}
		},

		update: function (e) {
			var type = (e && e.originalEvent && e.originalEvent.type),
				anyway = !type || type === 'orientationchange';

			if (anyway) {
				clearTimeout(didUpdate);

				didUpdate = null;
			}

			if (!F.isOpen || didUpdate) {
				return;
			}

			didUpdate = setTimeout(function () {
				var current = F.current;

				if (!current || F.isClosing) {
					return;
				}

				F.wrap.removeClass('fancybox-tmp');

				if (anyway || type === 'load' || (type === 'resize' && current.autoResize)) {
					F._setDimension();
				}

				if (!(type === 'scroll' && current.canShrink)) {
					F.reposition(e);
				}

				F.trigger('onUpdate');

				didUpdate = null;

			}, (anyway && !isTouch ? 0 : 300));
		},

		// Shrink content to fit inside viewport or restore if resized
		toggle: function (action) {
			if (F.isOpen) {
				F.current.fitToView = $.type(action) === "boolean" ? action : !F.current.fitToView;

				// Help browser to restore document dimensions
				if (isTouch) {
					F.wrap.removeAttr('style').addClass('fancybox-tmp');

					F.trigger('onUpdate');
				}

				F.update();
			}
		},

		hideLoading: function () {
			D.unbind('.loading');

			$('#fancybox-loading').remove();
		},

		showLoading: function () {
			var el, viewport;

			F.hideLoading();

			el = $('<div id="fancybox-loading"><div></div></div>').click(F.cancel).appendTo('body');

			// If user will press the escape-button, the request will be canceled
			D.bind('keydown.loading', function (e) {
				if ((e.which || e.keyCode) === 27) {
					e.preventDefault();

					F.cancel();
				}
			});

			if (!F.defaults.fixed) {
				viewport = F.getViewport();

				el.css({
					position: 'absolute',
					top: (viewport.h * 0.5) + viewport.y,
					left: (viewport.w * 0.5) + viewport.x
				});
			}

			F.trigger('onLoading');
		},

		getViewport: function () {
			var locked = (F.current && F.current.locked) || false,
				rez = {
					x: W.scrollLeft(),
					y: W.scrollTop()
				};

			if (locked && locked.length) {
				rez.w = locked[0].clientWidth;
				rez.h = locked[0].clientHeight;

			} else {
				// See https://bugs.jquery.com/ticket/6724
				rez.w = isTouch && window.innerWidth ? window.innerWidth : W.width();
				rez.h = isTouch && window.innerHeight ? window.innerHeight : W.height();
			}

			return rez;
		},

		// Unbind the keyboard / clicking actions
		unbindEvents: function () {
			if (F.wrap && isQuery(F.wrap)) {
				F.wrap.unbind('.fb');
			}

			D.unbind('.fb');
			W.unbind('.fb');
		},

		bindEvents: function () {
			var current = F.current,
				keys;

			if (!current) {
				return;
			}

			// Changing document height on iOS devices triggers a 'resize' event,
			// that can change document height... repeating infinitely
			W.bind('orientationchange.fb' + (isTouch ? '' : ' resize.fb') + (current.autoCenter && !current.locked ? ' scroll.fb' : ''), F.update);

			keys = current.keys;

			if (keys) {
				D.bind('keydown.fb', function (e) {
					var code = e.which || e.keyCode,
						target = e.target || e.srcElement;

					// Skip esc key if loading, because showLoading will cancel preloading
					if (code === 27 && F.coming) {
						return false;
					}

					// Ignore key combinations and key events within form elements
					if (!e.ctrlKey && !e.altKey && !e.shiftKey && !e.metaKey && !(target && (target.type || $(target).is('[contenteditable]')))) {
						$.each(keys, function (i, val) {
							if (current.group.length > 1 && val[code] !== undefined) {
								F[i](val[code]);

								e.preventDefault();
								return false;
							}

							if ($.inArray(code, val) > -1) {
								F[i]();

								e.preventDefault();
								return false;
							}
						});
					}
				});
			}

			if ($.fn.mousewheel && current.mouseWheel) {
				F.wrap.bind('mousewheel.fb', function (e, delta, deltaX, deltaY) {
					var target = e.target || null,
						parent = $(target),
						canScroll = false;

					while (parent.length) {
						if (canScroll || parent.is('.fancybox-skin') || parent.is('.fancybox-wrap')) {
							break;
						}

						canScroll = isScrollable(parent[0]);
						parent = $(parent).parent();
					}

					if (delta !== 0 && !canScroll) {
						if (F.group.length > 1 && !current.canShrink) {
							if (deltaY > 0 || deltaX > 0) {
								F.prev(deltaY > 0 ? 'down' : 'left');

							} else if (deltaY < 0 || deltaX < 0) {
								F.next(deltaY < 0 ? 'up' : 'right');
							}

							e.preventDefault();
						}
					}
				});
			}
		},

		trigger: function (event, o) {
			var ret, obj = o || F.coming || F.current;

			if (obj) {
				if ($.isFunction(obj[event])) {
					ret = obj[event].apply(obj, Array.prototype.slice.call(arguments, 1));
				}

				if (ret === false) {
					return false;
				}

				if (obj.helpers) {
					$.each(obj.helpers, function (helper, opts) {
						if (opts && F.helpers[helper] && $.isFunction(F.helpers[helper][event])) {
							F.helpers[helper][event]($.extend(true, {}, F.helpers[helper].defaults, opts), obj);
						}
					});
				}
			}

			D.trigger(event);
		},

		isImage: function (str) {
			return isString(str) && str.match(/(^data:image\/.*,)|(\.(jp(e|g|eg)|gif|png|bmp|webp|svg)((\?|#).*)?$)/i);
		},

		isSWF: function (str) {
			return isString(str) && str.match(/\.(swf)((\?|#).*)?$/i);
		},

		_start: function (index) {
			var coming = {},
				obj,
				href,
				type,
				margin,
				padding;

			index = getScalar(index);
			obj = F.group[index] || null;

			if (!obj) {
				return false;
			}

			coming = $.extend(true, {}, F.opts, obj);

			// Convert margin and padding properties to array - top, right, bottom, left
			margin = coming.margin;
			padding = coming.padding;

			if ($.type(margin) === 'number') {
				coming.margin = [margin, margin, margin, margin];
			}

			if ($.type(padding) === 'number') {
				coming.padding = [padding, padding, padding, padding];
			}

			// 'modal' propery is just a shortcut
			if (coming.modal) {
				$.extend(true, coming, {
					closeBtn: false,
					closeClick: false,
					nextClick: false,
					arrows: false,
					mouseWheel: false,
					keys: null,
					helpers: {
						overlay: {
							closeClick: false
						}
					}
				});
			}

			// 'autoSize' property is a shortcut, too
			if (coming.autoSize) {
				coming.autoWidth = coming.autoHeight = true;
			}

			if (coming.width === 'auto') {
				coming.autoWidth = true;
			}

			if (coming.height === 'auto') {
				coming.autoHeight = true;
			}

			/*
			 * Add reference to the group, so it`s possible to access from callbacks, example:
			 * afterLoad : function() {
			 *     this.title = 'Image ' + (this.index + 1) + ' of ' + this.group.length + (this.title ? ' - ' + this.title : '');
			 * }
			 */

			coming.group = F.group;
			coming.index = index;

			// Give a chance for callback or helpers to update coming item (type, title, etc)
			F.coming = coming;

			if (false === F.trigger('beforeLoad')) {
				F.coming = null;

				return;
			}

			type = coming.type;
			href = coming.href;

			if (!type) {
				F.coming = null;

				//If we can not determine content type then drop silently or display next/prev item if looping through gallery
				if (F.current && F.router && F.router !== 'jumpto') {
					F.current.index = index;

					return F[F.router](F.direction);
				}

				return false;
			}

			F.isActive = true;

			if (type === 'image' || type === 'swf') {
				coming.autoHeight = coming.autoWidth = false;
				coming.scrolling = 'visible';
			}

			if (type === 'image') {
				coming.aspectRatio = true;
			}

			if (type === 'iframe' && isTouch) {
				coming.scrolling = 'scroll';
			}

			// Build the neccessary markup
			coming.wrap = $(coming.tpl.wrap).addClass('fancybox-' + (isTouch ? 'mobile' : 'desktop') + ' fancybox-type-' + type + ' fancybox-tmp ' + coming.wrapCSS).appendTo(coming.parent || 'body');

			$.extend(coming, {
				skin: $('.fancybox-skin', coming.wrap),
				outer: $('.fancybox-outer', coming.wrap),
				inner: $('.fancybox-inner', coming.wrap)
			});

			$.each(["Top", "Right", "Bottom", "Left"], function (i, v) {
				coming.skin.css('padding' + v, getValue(coming.padding[i]));
			});

			F.trigger('onReady');

			// Check before try to load; 'inline' and 'html' types need content, others - href
			if (type === 'inline' || type === 'html') {
				if (!coming.content || !coming.content.length) {
					return F._error('content');
				}

			} else if (!href) {
				return F._error('href');
			}

			if (type === 'image') {
				F._loadImage();

			} else if (type === 'ajax') {
				F._loadAjax();

			} else if (type === 'iframe') {
				F._loadIframe();

			} else {
				F._afterLoad();
			}
		},

		_error: function (type) {
			$.extend(F.coming, {
				type: 'html',
				autoWidth: true,
				autoHeight: true,
				minWidth: 0,
				minHeight: 0,
				scrolling: 'no',
				hasError: type,
				content: F.coming.tpl.error
			});

			F._afterLoad();
		},

		_loadImage: function () {
			// Reset preload image so it is later possible to check "complete" property
			var img = F.imgPreload = new Image();

			img.onload = function () {
				this.onload = this.onerror = null;

				F.coming.width = this.width / F.opts.pixelRatio;
				F.coming.height = this.height / F.opts.pixelRatio;

				F._afterLoad();
			};

			img.onerror = function () {
				this.onload = this.onerror = null;

				F._error('image');
			};

			img.src = F.coming.href;

			if (img.complete !== true) {
				F.showLoading();
			}
		},

		_loadAjax: function () {
			var coming = F.coming;

			F.showLoading();

			F.ajaxLoad = $.ajax($.extend({}, coming.ajax, {
				url: coming.href,
				error: function (jqXHR, textStatus) {
					if (F.coming && textStatus !== 'abort') {
						F._error('ajax', jqXHR);

					} else {
						F.hideLoading();
					}
				},
				success: function (data, textStatus) {
					if (textStatus === 'success') {
						coming.content = data;

						F._afterLoad();
					}
				}
			}));
		},

		_loadIframe: function () {
			var coming = F.coming,
				iframe = $(coming.tpl.iframe.replace(/\{rnd\}/g, new Date().getTime()))
				.attr('scrolling', isTouch ? 'auto' : coming.iframe.scrolling)
				.attr('src', coming.href);

			// This helps IE
			$(coming.wrap).bind('onReset', function () {
				try {
					$(this).find('iframe').hide().attr('src', '//about:blank').end().empty();
				} catch (e) {}
			});

			if (coming.iframe.preload) {
				F.showLoading();

				iframe.one('load', function () {
					$(this).data('ready', 1);

					// iOS will lose scrolling if we resize
					if (!isTouch) {
						$(this).bind('load.fb', F.update);
					}

					// Without this trick:
					//   - iframe won't scroll on iOS devices
					//   - IE7 sometimes displays empty iframe
					$(this).parents('.fancybox-wrap').width('100%').removeClass('fancybox-tmp').show();

					F._afterLoad();
				});
			}

			coming.content = iframe.appendTo(coming.inner);

			if (!coming.iframe.preload) {
				F._afterLoad();
			}
		},

		_preloadImages: function () {
			var group = F.group,
				current = F.current,
				len = group.length,
				cnt = current.preload ? Math.min(current.preload, len - 1) : 0,
				item,
				i;

			for (i = 1; i <= cnt; i += 1) {
				item = group[(current.index + i) % len];

				if (item.type === 'image' && item.href) {
					new Image().src = item.href;
				}
			}
		},

		_afterLoad: function () {
			var coming = F.coming,
				previous = F.current,
				placeholder = 'fancybox-placeholder',
				current,
				content,
				type,
				scrolling,
				href,
				embed;

			F.hideLoading();

			if (!coming || F.isActive === false) {
				return;
			}

			if (false === F.trigger('afterLoad', coming, previous)) {
				coming.wrap.stop(true).trigger('onReset').remove();

				F.coming = null;

				return;
			}

			if (previous) {
				F.trigger('beforeChange', previous);

				previous.wrap.stop(true).removeClass('fancybox-opened')
					.find('.fancybox-item, .fancybox-nav')
					.remove();
			}

			F.unbindEvents();

			current = coming;
			content = coming.content;
			type = coming.type;
			scrolling = coming.scrolling;

			$.extend(F, {
				wrap: current.wrap,
				skin: current.skin,
				outer: current.outer,
				inner: current.inner,
				current: current,
				previous: previous
			});

			href = current.href;

			switch (type) {
				case 'inline':
				case 'ajax':
				case 'html':
					if (current.selector) {
						content = $('<div>').html(content).find(current.selector);

					} else if (isQuery(content)) {
						if (!content.data(placeholder)) {
							content.data(placeholder, $('<div class="' + placeholder + '"></div>').insertAfter(content).hide());
						}

						content = content.show().detach();

						current.wrap.bind('onReset', function () {
							if ($(this).find(content).length) {
								content.hide().replaceAll(content.data(placeholder)).data(placeholder, false);
							}
						});
					}
					break;

				case 'image':
					content = current.tpl.image.replace(/\{href\}/g, href);
					break;

				case 'swf':
					content = '<object id="fancybox-swf" classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" width="100%" height="100%"><param name="movie" value="' + href + '"></param>';
					embed = '';

					$.each(current.swf, function (name, val) {
						content += '<param name="' + name + '" value="' + val + '"></param>';
						embed += ' ' + name + '="' + val + '"';
					});

					content += '<embed src="' + href + '" type="application/x-shockwave-flash" width="100%" height="100%"' + embed + '></embed></object>';
					break;
			}

			if (!(isQuery(content) && content.parent().is(current.inner))) {
				current.inner.append(content);
			}

			// Give a chance for helpers or callbacks to update elements
			F.trigger('beforeShow');

			// Set scrolling before calculating dimensions
			current.inner.css('overflow', scrolling === 'yes' ? 'scroll' : (scrolling === 'no' ? 'hidden' : scrolling));

			// Set initial dimensions and start position
			F._setDimension();

			F.reposition();

			F.isOpen = false;
			F.coming = null;

			F.bindEvents();

			if (!F.isOpened) {
				$('.fancybox-wrap').not(current.wrap).stop(true).trigger('onReset').remove();

			} else if (previous.prevMethod) {
				F.transitions[previous.prevMethod]();
			}

			F.transitions[F.isOpened ? current.nextMethod : current.openMethod]();

			F._preloadImages();
		},

		_setDimension: function () {
			var viewport = F.getViewport(),
				steps = 0,
				canShrink = false,
				canExpand = false,
				wrap = F.wrap,
				skin = F.skin,
				inner = F.inner,
				current = F.current,
				width = current.width,
				height = current.height,
				minWidth = current.minWidth,
				minHeight = current.minHeight,
				maxWidth = current.maxWidth,
				maxHeight = current.maxHeight,
				scrolling = current.scrolling,
				scrollOut = current.scrollOutside ? current.scrollbarWidth : 0,
				margin = current.margin,
				wMargin = getScalar(margin[1] + margin[3]),
				hMargin = getScalar(margin[0] + margin[2]),
				wPadding,
				hPadding,
				wSpace,
				hSpace,
				origWidth,
				origHeight,
				origMaxWidth,
				origMaxHeight,
				ratio,
				width_,
				height_,
				maxWidth_,
				maxHeight_,
				iframe,
				body;

			// Reset dimensions so we could re-check actual size
			wrap.add(skin).add(inner).width('auto').height('auto').removeClass('fancybox-tmp');

			wPadding = getScalar(skin.outerWidth(true) - skin.width());
			hPadding = getScalar(skin.outerHeight(true) - skin.height());

			// Any space between content and viewport (margin, padding, border, title)
			wSpace = wMargin + wPadding;
			hSpace = hMargin + hPadding;

			origWidth = isPercentage(width) ? (viewport.w - wSpace) * getScalar(width) / 100 : width;
			origHeight = isPercentage(height) ? (viewport.h - hSpace) * getScalar(height) / 100 : height;

			if (current.type === 'iframe') {
				iframe = current.content;

				if (current.autoHeight && iframe.data('ready') === 1) {
					try {
						if (iframe[0].contentWindow.document.location) {
							inner.width(origWidth).height(9999);

							body = iframe.contents().find('body');

							if (scrollOut) {
								body.css('overflow-x', 'hidden');
							}

							origHeight = body.outerHeight(true);
						}

					} catch (e) {}
				}

			} else if (current.autoWidth || current.autoHeight) {
				inner.addClass('fancybox-tmp');

				// Set width or height in case we need to calculate only one dimension
				if (!current.autoWidth) {
					inner.width(origWidth);
				}

				if (!current.autoHeight) {
					inner.height(origHeight);
				}

				if (current.autoWidth) {
					origWidth = inner.width();
				}

				if (current.autoHeight) {
					origHeight = inner.height();
				}

				inner.removeClass('fancybox-tmp');
			}

			width = getScalar(origWidth);
			height = getScalar(origHeight);

			ratio = origWidth / origHeight;

			// Calculations for the content
			minWidth = getScalar(isPercentage(minWidth) ? getScalar(minWidth, 'w') - wSpace : minWidth);
			maxWidth = getScalar(isPercentage(maxWidth) ? getScalar(maxWidth, 'w') - wSpace : maxWidth);

			minHeight = getScalar(isPercentage(minHeight) ? getScalar(minHeight, 'h') - hSpace : minHeight);
			maxHeight = getScalar(isPercentage(maxHeight) ? getScalar(maxHeight, 'h') - hSpace : maxHeight);

			// These will be used to determine if wrap can fit in the viewport
			origMaxWidth = maxWidth;
			origMaxHeight = maxHeight;

			if (current.fitToView) {
				maxWidth = Math.min(viewport.w - wSpace, maxWidth);
				maxHeight = Math.min(viewport.h - hSpace, maxHeight);
			}

			maxWidth_ = viewport.w - wMargin;
			maxHeight_ = viewport.h - hMargin;

			if (current.aspectRatio) {
				if (width > maxWidth) {
					width = maxWidth;
					height = getScalar(width / ratio);
				}

				if (height > maxHeight) {
					height = maxHeight;
					width = getScalar(height * ratio);
				}

				if (width < minWidth) {
					width = minWidth;
					height = getScalar(width / ratio);
				}

				if (height < minHeight) {
					height = minHeight;
					width = getScalar(height * ratio);
				}

			} else {
				width = Math.max(minWidth, Math.min(width, maxWidth));

				if (current.autoHeight && current.type !== 'iframe') {
					inner.width(width);

					height = inner.height();
				}

				height = Math.max(minHeight, Math.min(height, maxHeight));
			}

			// Try to fit inside viewport (including the title)
			if (current.fitToView) {
				inner.width(width).height(height);

				wrap.width(width + wPadding);

				// Real wrap dimensions
				width_ = wrap.width();
				height_ = wrap.height();

				if (current.aspectRatio) {
					while ((width_ > maxWidth_ || height_ > maxHeight_) && width > minWidth && height > minHeight) {
						if (steps++ > 19) {
							break;
						}

						height = Math.max(minHeight, Math.min(maxHeight, height - 10));
						width = getScalar(height * ratio);

						if (width < minWidth) {
							width = minWidth;
							height = getScalar(width / ratio);
						}

						if (width > maxWidth) {
							width = maxWidth;
							height = getScalar(width / ratio);
						}

						inner.width(width).height(height);

						wrap.width(width + wPadding);

						width_ = wrap.width();
						height_ = wrap.height();
					}

				} else {
					width = Math.max(minWidth, Math.min(width, width - (width_ - maxWidth_)));
					height = Math.max(minHeight, Math.min(height, height - (height_ - maxHeight_)));
				}
			}

			if (scrollOut && scrolling === 'auto' && height < origHeight && (width + wPadding + scrollOut) < maxWidth_) {
				width += scrollOut;
			}

			inner.width(width).height(height);

			wrap.width(width + wPadding);

			width_ = wrap.width();
			height_ = wrap.height();

			canShrink = (width_ > maxWidth_ || height_ > maxHeight_) && width > minWidth && height > minHeight;
			canExpand = current.aspectRatio ? (width < origMaxWidth && height < origMaxHeight && width < origWidth && height < origHeight) : ((width < origMaxWidth || height < origMaxHeight) && (width < origWidth || height < origHeight));

			$.extend(current, {
				dim: {
					width: getValue(width_),
					height: getValue(height_)
				},
				origWidth: origWidth,
				origHeight: origHeight,
				canShrink: canShrink,
				canExpand: canExpand,
				wPadding: wPadding,
				hPadding: hPadding,
				wrapSpace: height_ - skin.outerHeight(true),
				skinSpace: skin.height() - height
			});

			if (!iframe && current.autoHeight && height > minHeight && height < maxHeight && !canExpand) {
				inner.height('auto');
			}
		},

		_getPosition: function (onlyAbsolute) {
			var current = F.current,
				viewport = F.getViewport(),
				margin = current.margin,
				width = F.wrap.width() + margin[1] + margin[3],
				height = F.wrap.height() + margin[0] + margin[2],
				rez = {
					position: 'absolute',
					top: margin[0],
					left: margin[3]
				};

			if (current.autoCenter && current.fixed && !onlyAbsolute && height <= viewport.h && width <= viewport.w) {
				rez.position = 'fixed';

			} else if (!current.locked) {
				rez.top += viewport.y;
				rez.left += viewport.x;
			}

			rez.top = getValue(Math.max(rez.top, rez.top + ((viewport.h - height) * current.topRatio)));
			rez.left = getValue(Math.max(rez.left, rez.left + ((viewport.w - width) * current.leftRatio)));

			return rez;
		},

		_afterZoomIn: function () {
			var current = F.current;

			if (!current) {
				return;
			}

			F.isOpen = F.isOpened = true;

			F.wrap.css('overflow', 'visible').addClass('fancybox-opened');

			F.update();

			// Assign a click event
			if (current.closeClick || (current.nextClick && F.group.length > 1)) {
				F.inner.css('cursor', 'pointer').bind('click.fb', function (e) {
					if (!$(e.target).is('a') && !$(e.target).parent().is('a')) {
						e.preventDefault();

						F[current.closeClick ? 'close' : 'next']();
					}
				});
			}

			// Create a close button
			if (current.closeBtn) {
				$(current.tpl.closeBtn).appendTo(F.skin).bind('click.fb', function (e) {
					e.preventDefault();

					F.close();
				});
			}

			// Create navigation arrows
			if (current.arrows && F.group.length > 1) {
				if (current.loop || current.index > 0) {
					$(current.tpl.prev).appendTo(F.outer).bind('click.fb', F.prev);
				}

				if (current.loop || current.index < F.group.length - 1) {
					$(current.tpl.next).appendTo(F.outer).bind('click.fb', F.next);
				}
			}

			F.trigger('afterShow');

			// Stop the slideshow if this is the last item
			if (!current.loop && current.index === current.group.length - 1) {
				F.play(false);

			} else if (F.opts.autoPlay && !F.player.isActive) {
				F.opts.autoPlay = false;

				F.play();
			}
		},

		_afterZoomOut: function (obj) {
			obj = obj || F.current;

			$('.fancybox-wrap').trigger('onReset').remove();

			$.extend(F, {
				group: {},
				opts: {},
				router: false,
				current: null,
				isActive: false,
				isOpened: false,
				isOpen: false,
				isClosing: false,
				wrap: null,
				skin: null,
				outer: null,
				inner: null
			});

			F.trigger('afterClose', obj);
		}
	});

	/*
	 *	Default transitions
	 */

	F.transitions = {
		getOrigPosition: function () {
			var current = F.current,
				element = current.element,
				orig = current.orig,
				pos = {},
				width = 50,
				height = 50,
				hPadding = current.hPadding,
				wPadding = current.wPadding,
				viewport = F.getViewport();

			if (!orig && current.isDom && element.is(':visible')) {
				orig = element.find('img:first');

				if (!orig.length) {
					orig = element;
				}
			}

			if (isQuery(orig)) {
				pos = orig.offset();

				if (orig.is('img')) {
					width = orig.outerWidth();
					height = orig.outerHeight();
				}

			} else {
				pos.top = viewport.y + (viewport.h - height) * current.topRatio;
				pos.left = viewport.x + (viewport.w - width) * current.leftRatio;
			}

			if (F.wrap.css('position') === 'fixed' || current.locked) {
				pos.top -= viewport.y;
				pos.left -= viewport.x;
			}

			pos = {
				top: getValue(pos.top - hPadding * current.topRatio),
				left: getValue(pos.left - wPadding * current.leftRatio),
				width: getValue(width + wPadding),
				height: getValue(height + hPadding)
			};

			return pos;
		},

		step: function (now, fx) {
			var ratio,
				padding,
				value,
				prop = fx.prop,
				current = F.current,
				wrapSpace = current.wrapSpace,
				skinSpace = current.skinSpace;

			if (prop === 'width' || prop === 'height') {
				ratio = fx.end === fx.start ? 1 : (now - fx.start) / (fx.end - fx.start);

				if (F.isClosing) {
					ratio = 1 - ratio;
				}

				padding = prop === 'width' ? current.wPadding : current.hPadding;
				value = now - padding;

				F.skin[prop](getScalar(prop === 'width' ? value : value - (wrapSpace * ratio)));
				F.inner[prop](getScalar(prop === 'width' ? value : value - (wrapSpace * ratio) - (skinSpace * ratio)));
			}
		},

		zoomIn: function () {
			var current = F.current,
				startPos = current.pos,
				effect = current.openEffect,
				elastic = effect === 'elastic',
				endPos = $.extend({
					opacity: 1
				}, startPos);

			// Remove "position" property that breaks older IE
			delete endPos.position;

			if (elastic) {
				startPos = this.getOrigPosition();

				if (current.openOpacity) {
					startPos.opacity = 0.1;
				}

			} else if (effect === 'fade') {
				startPos.opacity = 0.1;
			}

			F.wrap.css(startPos).animate(endPos, {
				duration: effect === 'none' ? 0 : current.openSpeed,
				easing: current.openEasing,
				step: elastic ? this.step : null,
				complete: F._afterZoomIn
			});
		},

		zoomOut: function () {
			var current = F.current,
				effect = current.closeEffect,
				elastic = effect === 'elastic',
				endPos = {
					opacity: 0.1
				};

			if (elastic) {
				endPos = this.getOrigPosition();

				if (current.closeOpacity) {
					endPos.opacity = 0.1;
				}
			}

			F.wrap.animate(endPos, {
				duration: effect === 'none' ? 0 : current.closeSpeed,
				easing: current.closeEasing,
				step: elastic ? this.step : null,
				complete: F._afterZoomOut
			});
		},

		changeIn: function () {
			var current = F.current,
				effect = current.nextEffect,
				startPos = current.pos,
				endPos = {
					opacity: 1
				},
				direction = F.direction,
				distance = 200,
				field;

			startPos.opacity = 0.1;

			if (effect === 'elastic') {
				field = direction === 'down' || direction === 'up' ? 'top' : 'left';

				if (direction === 'down' || direction === 'right') {
					startPos[field] = getValue(getScalar(startPos[field]) - distance);
					endPos[field] = '+=' + distance + 'px';

				} else {
					startPos[field] = getValue(getScalar(startPos[field]) + distance);
					endPos[field] = '-=' + distance + 'px';
				}
			}

			// Workaround for https://bugs.jquery.com/ticket/12273
			if (effect === 'none') {
				F._afterZoomIn();

			} else {
				F.wrap.css(startPos).animate(endPos, {
					duration: current.nextSpeed,
					easing: current.nextEasing,
					complete: F._afterZoomIn
				});
			}
		},

		changeOut: function () {
			var previous = F.previous,
				effect = previous.prevEffect,
				endPos = {
					opacity: 0.1
				},
				direction = F.direction,
				distance = 200;

			if (effect === 'elastic') {
				endPos[direction === 'down' || direction === 'up' ? 'top' : 'left'] = (direction === 'up' || direction === 'left' ? '-' : '+') + '=' + distance + 'px';
			}

			previous.wrap.animate(endPos, {
				duration: effect === 'none' ? 0 : previous.prevSpeed,
				easing: previous.prevEasing,
				complete: function () {
					$(this).trigger('onReset').remove();
				}
			});
		}
	};

	/*
	 *	Overlay helper
	 */

	F.helpers.overlay = {
		defaults: {
			closeClick: true, // if true, fancyBox will be closed when user clicks on the overlay
			speedOut: 200, // duration of fadeOut animation
			showEarly: true, // indicates if should be opened immediately or wait until the content is ready
			css: {}, // custom CSS properties
			locked: !isTouch, // if true, the content will be locked into overlay
			fixed: true // if false, the overlay CSS position property will not be set to "fixed"
		},

		overlay: null, // current handle
		fixed: false, // indicates if the overlay has position "fixed"
		el: $('html'), // element that contains "the lock"

		// Public methods
		create: function (opts) {
			var parent;

			opts = $.extend({}, this.defaults, opts);

			if (this.overlay) {
				this.close();
			}

			parent = F.coming ? F.coming.parent : opts.parent;

			this.overlay = $('<div class="fancybox-overlay"></div>').appendTo(parent && parent.lenth ? parent : 'body');
			this.fixed = false;

			if (opts.fixed && F.defaults.fixed) {
				this.overlay.addClass('fancybox-overlay-fixed');

				this.fixed = true;
			}
		},

		open: function (opts) {
			var that = this;

			opts = $.extend({}, this.defaults, opts);

			if (this.overlay) {
				this.overlay.unbind('.overlay').width('auto').height('auto');

			} else {
				this.create(opts);
			}

			if (!this.fixed) {
				W.bind('resize.overlay', $.proxy(this.update, this));

				this.update();
			}

			if (opts.closeClick) {
				this.overlay.bind('click.overlay', function (e) {
					if ($(e.target).hasClass('fancybox-overlay')) {
						if (F.isActive) {
							F.close();
						} else {
							that.close();
						}

						return false;
					}
				});
			}

			this.overlay.css(opts.css).show();
		},

		close: function () {
			W.unbind('resize.overlay');

			if (this.el.hasClass('fancybox-lock')) {
				$('.fancybox-margin').removeClass('fancybox-margin');

				this.el.removeClass('fancybox-lock');

				W.scrollTop(this.scrollV).scrollLeft(this.scrollH);
			}

			$('.fancybox-overlay').remove().hide();

			$.extend(this, {
				overlay: null,
				fixed: false
			});
		},

		// Private, callbacks

		update: function () {
			var width = '100%',
				offsetWidth;

			// Reset width/height so it will not mess
			this.overlay.width(width).height('100%');

			// jQuery does not return reliable result for IE
			if (IE) {
				offsetWidth = Math.max(document.documentElement.offsetWidth, document.body.offsetWidth);

				if (D.width() > offsetWidth) {
					width = D.width();
				}

			} else if (D.width() > W.width()) {
				width = D.width();
			}

			this.overlay.width(width).height(D.height());
		},

		// This is where we can manipulate DOM, because later it would cause iframes to reload
		onReady: function (opts, obj) {
			var overlay = this.overlay;

			$('.fancybox-overlay').stop(true, true);

			if (!overlay) {
				this.create(opts);
			}

			if (opts.locked && this.fixed && obj.fixed) {
				obj.locked = this.overlay.append(obj.wrap);
				obj.fixed = false;
			}

			if (opts.showEarly === true) {
				this.beforeShow.apply(this, arguments);
			}
		},

		beforeShow: function (opts, obj) {
			if (obj.locked && !this.el.hasClass('fancybox-lock')) {
				if (this.fixPosition !== false) {
					$('*').filter(function () {
						return ($(this).css('position') === 'fixed' && !$(this).hasClass("fancybox-overlay") && !$(this).hasClass("fancybox-wrap"));
					}).addClass('fancybox-margin');
				}

				this.el.addClass('fancybox-margin');

				this.scrollV = W.scrollTop();
				this.scrollH = W.scrollLeft();

				this.el.addClass('fancybox-lock');

				W.scrollTop(this.scrollV).scrollLeft(this.scrollH);
			}

			this.open(opts);
		},

		onUpdate: function () {
			if (!this.fixed) {
				this.update();
			}
		},

		afterClose: function (opts) {
			// Remove overlay if exists and fancyBox is not opening
			// (e.g., it is not being open using afterClose callback)
			if (this.overlay && !F.coming) {
				this.overlay.fadeOut(opts.speedOut, $.proxy(this.close, this));
			}
		}
	};

	/*
	 *	Title helper
	 */

	F.helpers.title = {
		defaults: {
			type: 'float', // 'float', 'inside', 'outside' or 'over',
			position: 'bottom' // 'top' or 'bottom'
		},

		beforeShow: function (opts) {
			var current = F.current,
				text = current.title,
				type = opts.type,
				title,
				target;

			if ($.isFunction(text)) {
				text = text.call(current.element, current);
			}

			if (!isString(text) || $.trim(text) === '') {
				return;
			}

			title = $('<div class="fancybox-title fancybox-title-' + type + '-wrap">' + text + '</div>');

			switch (type) {
				case 'inside':
					target = F.skin;
					break;

				case 'outside':
					target = F.wrap;
					break;

				case 'over':
					target = F.inner;
					break;

				default: // 'float'
					target = F.skin;

					title.appendTo('body');

					if (IE) {
						title.width(title.width());
					}

					title.wrapInner('<span class="child"></span>');

					//Increase bottom margin so this title will also fit into viewport
					F.current.margin[2] += Math.abs(getScalar(title.css('margin-bottom')));
					break;
			}

			title[(opts.position === 'top' ? 'prependTo' : 'appendTo')](target);
		}
	};

	// jQuery plugin initialization
	$.fn.fancybox = function (options) {
		var index,
			that = $(this),
			selector = this.selector || '',
			run = function (e) {
				var what = $(this).blur(),
					idx = index,
					relType, relVal;

				if (!(e.ctrlKey || e.altKey || e.shiftKey || e.metaKey) && !what.is('.fancybox-wrap')) {
					relType = options.groupAttr || 'data-fancybox-group';
					relVal = what.attr(relType);

					if (!relVal) {
						relType = 'rel';
						relVal = what.get(0)[relType];
					}

					if (relVal && relVal !== '' && relVal !== 'nofollow') {
						what = selector.length ? $(selector) : that;
						what = what.filter('[' + relType + '="' + relVal + '"]');
						idx = what.index(this);
					}

					options.index = idx;

					// Stop an event from bubbling if everything is fine
					if (F.open(what, options) !== false) {
						e.preventDefault();
					}
				}
			};

		options = options || {};
		index = options.index || 0;

		if (!selector || options.live === false) {
			that.unbind('click.fb-start').bind('click.fb-start', run);

		} else {
			D.undelegate(selector, 'click.fb-start').delegate(selector + ":not('.fancybox-item, .fancybox-nav')", 'click.fb-start', run);
		}

		this.filter('[data-fancybox-start=1]').trigger('click');

		return this;
	};

	// Tests that need a body at doc ready
	D.ready(function () {
		var w1, w2;

		if ($.scrollbarWidth === undefined) {
			// http://benalman.com/projects/jquery-misc-plugins/#scrollbarwidth
			$.scrollbarWidth = function () {
				var parent = $('<div style="width:50px;height:50px;overflow:auto"><div/></div>').appendTo('body'),
					child = parent.children(),
					width = child.innerWidth() - child.height(99).innerWidth();

				parent.remove();

				return width;
			};
		}

		if ($.support.fixedPosition === undefined) {
			$.support.fixedPosition = (function () {
				var elem = $('<div style="position:fixed;top:20px;"></div>').appendTo('body'),
					fixed = (elem[0].offsetTop === 20 || elem[0].offsetTop === 15);

				elem.remove();

				return fixed;
			}());
		}

		$.extend(F.defaults, {
			scrollbarWidth: $.scrollbarWidth(),
			fixed: $.support.fixedPosition,
			parent: $('body')
		});

		//Get real width of page scroll-bar
		w1 = $(window).width();

		H.addClass('fancybox-lock-test');

		w2 = $(window).width();

		H.removeClass('fancybox-lock-test');

		$("<style type='text/css'>.fancybox-margin{margin-right:" + (w2 - w1) + "px;}</style>").appendTo("head");
	});

}(window, document, jQuery));
! function (e, t, n, i) {
	"use strict";
	var o = n("html"),
		a = n(e),
		r = n(t),
		s = n.fancybox = function () {
			s.open.apply(this, arguments)
		},
		l = navigator.userAgent.match(/msie/i),
		c = null,
		d = t.createTouch !== i,
		p = function (e) {
			return e && e.hasOwnProperty && e instanceof n
		},
		h = function (e) {
			return e && "string" === n.type(e)
		},
		f = function (e) {
			return h(e) && e.indexOf("%") > 0
		},
		u = function (e) {
			return e && !(e.style.overflow && "hidden" === e.style.overflow) && (e.clientWidth && e.scrollWidth > e.clientWidth || e.clientHeight && e.scrollHeight > e.clientHeight)
		},
		g = function (e, t) {
			var n = parseInt(e, 10) || 0;
			return t && f(e) && (n = s.getViewport()[t] / 100 * n), Math.ceil(n)
		},
		m = function (e, t) {
			return g(e, t) + "px"
		};
	n.extend(s, {
		version: "2.1.5",
		defaults: {
			padding: 15,
			margin: 20,
			width: 800,
			height: 600,
			minWidth: 100,
			minHeight: 100,
			maxWidth: 9999,
			maxHeight: 9999,
			pixelRatio: 1,
			autoSize: !0,
			autoHeight: !1,
			autoWidth: !1,
			autoResize: !0,
			autoCenter: !d,
			fitToView: !0,
			aspectRatio: !1,
			topRatio: .5,
			leftRatio: .5,
			scrolling: "auto",
			wrapCSS: "",
			arrows: !0,
			closeBtn: !0,
			closeClick: !1,
			nextClick: !1,
			mouseWheel: !0,
			autoPlay: !1,
			playSpeed: 3e3,
			preload: 3,
			modal: !1,
			loop: !0,
			ajax: {
				dataType: "html",
				headers: {
					"X-fancyBox": !0
				}
			},
			iframe: {
				scrolling: "no",
				preload: !0
			},
			swf: {
				wmode: "transparent",
				allowfullscreen: "true",
				allowscriptaccess: "always"
			},
			keys: {
				next: {
					13: "left",
					34: "up",
					39: "left",
					40: "up"
				},
				prev: {
					8: "right",
					33: "down",
					37: "right",
					38: "down"
				},
				close: [27],
				play: [32],
				toggle: [70]
			},
			direction: {
				next: "left",
				prev: "right"
			},
			scrollOutside: !0,
			index: 0,
			type: null,
			href: null,
			content: null,
			title: null,
			tpl: {
				wrap: '<div class="fancybox-wrap" tabIndex="-1"><div class="fancybox-skin"><div class="fancybox-outer"><div class="fancybox-inner"></div></div></div></div>',
				image: '<img class="fancybox-image" src="{href}" alt="" />',
				iframe: '<iframe id="fancybox-frame{rnd}" name="fancybox-frame{rnd}" class="fancybox-iframe" frameborder="0" vspace="0" hspace="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen' + (l ? ' allowtransparency="true"' : "") + "></iframe>",
				error: '<p class="fancybox-error">The requested content cannot be loaded.<br/>Please try again later.</p>',
				closeBtn: '<a title="Close" class="fancybox-item fancybox-close" href="javascript:;"></a>',
				next: '<a title="Next" class="fancybox-nav fancybox-next" href="javascript:;"><span></span></a>',
				prev: '<a title="Previous" class="fancybox-nav fancybox-prev" href="javascript:;"><span></span></a>'
			},
			openEffect: "fade",
			openSpeed: 250,
			openEasing: "swing",
			openOpacity: !0,
			openMethod: "zoomIn",
			closeEffect: "fade",
			closeSpeed: 250,
			closeEasing: "swing",
			closeOpacity: !0,
			closeMethod: "zoomOut",
			nextEffect: "elastic",
			nextSpeed: 250,
			nextEasing: "swing",
			nextMethod: "changeIn",
			prevEffect: "elastic",
			prevSpeed: 250,
			prevEasing: "swing",
			prevMethod: "changeOut",
			helpers: {
				overlay: !0,
				title: !0
			},
			onCancel: n.noop,
			beforeLoad: n.noop,
			afterLoad: n.noop,
			beforeShow: n.noop,
			afterShow: n.noop,
			beforeChange: n.noop,
			beforeClose: n.noop,
			afterClose: n.noop
		},
		group: {},
		opts: {},
		previous: null,
		coming: null,
		current: null,
		isActive: !1,
		isOpen: !1,
		isOpened: !1,
		wrap: null,
		skin: null,
		outer: null,
		inner: null,
		player: {
			timer: null,
			isActive: !1
		},
		ajaxLoad: null,
		imgPreload: null,
		transitions: {},
		helpers: {},
		open: function (e, t) {
			return e && (n.isPlainObject(t) || (t = {}), !1 !== s.close(!0)) ? (n.isArray(e) || (e = p(e) ? n(e).get() : [e]), n.each(e, function (o, a) {
				var r, l, c, d, f, u, g, m = {};
				"object" === n.type(a) && (a.nodeType && (a = n(a)), p(a) ? (m = {
					href: a.data("fancybox-href") || a.attr("href"),
					title: a.data("fancybox-title") || a.attr("title"),
					isDom: !0,
					element: a
				}, n.metadata && n.extend(!0, m, a.metadata())) : m = a), r = t.href || m.href || (h(a) ? a : null), l = t.title !== i ? t.title : m.title || "", c = t.content || m.content, d = c ? "html" : t.type || m.type, !d && m.isDom && (d = a.data("fancybox-type"), d || (f = a.prop("class").match(/fancybox\.(\w+)/), d = f ? f[1] : null)), h(r) && (d || (s.isImage(r) ? d = "image" : s.isSWF(r) ? d = "swf" : "#" === r.charAt(0) ? d = "inline" : h(a) && (d = "html", c = a)), "ajax" === d && (u = r.split(/\s+/, 2), r = u.shift(), g = u.shift())), c || ("inline" === d ? r ? c = n(h(r) ? r.replace(/.*(?=#[^\s]+$)/, "") : r) : m.isDom && (c = a) : "html" === d ? c = r : d || r || !m.isDom || (d = "inline", c = a)), n.extend(m, {
					href: r,
					type: d,
					content: c,
					title: l,
					selector: g
				}), e[o] = m
			}), s.opts = n.extend(!0, {}, s.defaults, t), t.keys !== i && (s.opts.keys = t.keys ? n.extend({}, s.defaults.keys, t.keys) : !1), s.group = e, s._start(s.opts.index)) : void 0
		},
		cancel: function () {
			var e = s.coming;
			!1 !== s.trigger("onCancel") && (s.hideLoading(), e && (s.ajaxLoad && s.ajaxLoad.abort(), s.ajaxLoad = null, s.imgPreload && (s.imgPreload.onload = s.imgPreload.onerror = null), e.wrap && e.wrap.stop(!0, !0).trigger("onReset").remove(), s.coming = null, s.current || s._afterZoomOut(e)))
		},
		close: function (e) {
			s.cancel(), !1 !== s.trigger("beforeClose") && (s.unbindEvents(), s.isActive && (s.isOpen && e !== !0 ? (s.isOpen = s.isOpened = !1, s.isClosing = !0, n(".fancybox-item, .fancybox-nav").remove(), s.wrap.stop(!0, !0).removeClass("fancybox-opened"), s.transitions[s.current.closeMethod]()) : (n(".fancybox-wrap").stop(!0).trigger("onReset").remove(), s._afterZoomOut())))
		},
		play: function (e) {
			var t = function () {
					clearTimeout(s.player.timer)
				},
				n = function () {
					t(), s.current && s.player.isActive && (s.player.timer = setTimeout(s.next, s.current.playSpeed))
				},
				i = function () {
					t(), r.unbind(".player"), s.player.isActive = !1, s.trigger("onPlayEnd")
				},
				o = function () {
					s.current && (s.current.loop || s.current.index < s.group.length - 1) && (s.player.isActive = !0, r.bind({
						"onCancel.player beforeClose.player": i,
						"onUpdate.player": n,
						"beforeLoad.player": t
					}), n(), s.trigger("onPlayStart"))
				};
			e === !0 || !s.player.isActive && e !== !1 ? o() : i()
		},
		next: function (e) {
			var t = s.current;
			t && (h(e) || (e = t.direction.next), s.jumpto(t.index + 1, e, "next"))
		},
		prev: function (e) {
			var t = s.current;
			t && (h(e) || (e = t.direction.prev), s.jumpto(t.index - 1, e, "prev"))
		},
		jumpto: function (e, t, n) {
			var o = s.current;
			o && (e = g(e), s.direction = t || o.direction[e >= o.index ? "next" : "prev"], s.router = n || "jumpto", o.loop && (0 > e && (e = o.group.length + e % o.group.length), e %= o.group.length), o.group[e] !== i && (s.cancel(), s._start(e)))
		},
		reposition: function (e, t) {
			var i, o = s.current,
				a = o ? o.wrap : null;
			a && (i = s._getPosition(t), e && "scroll" === e.type ? (delete i.position, a.stop(!0, !0).animate(i, 200)) : (a.css(i), o.pos = n.extend({}, o.dim, i)))
		},
		update: function (e) {
			var t = e && e.originalEvent && e.originalEvent.type,
				n = !t || "orientationchange" === t;
			n && (clearTimeout(c), c = null), s.isOpen && !c && (c = setTimeout(function () {
				var i = s.current;
				i && !s.isClosing && (s.wrap.removeClass("fancybox-tmp"), (n || "load" === t || "resize" === t && i.autoResize) && s._setDimension(), "scroll" === t && i.canShrink || s.reposition(e), s.trigger("onUpdate"), c = null)
			}, n && !d ? 0 : 300))
		},
		toggle: function (e) {
			s.isOpen && (s.current.fitToView = "boolean" === n.type(e) ? e : !s.current.fitToView, d && (s.wrap.removeAttr("style").addClass("fancybox-tmp"), s.trigger("onUpdate")), s.update())
		},
		hideLoading: function () {
			r.unbind(".loading"), n("#fancybox-loading").remove()
		},
		showLoading: function () {
			var e, t;
			s.hideLoading(), e = n('<div id="fancybox-loading"><div></div></div>').click(s.cancel).appendTo("body"), r.bind("keydown.loading", function (e) {
				27 === (e.which || e.keyCode) && (e.preventDefault(), s.cancel())
			}), s.defaults.fixed || (t = s.getViewport(), e.css({
				position: "absolute",
				top: .5 * t.h + t.y,
				left: .5 * t.w + t.x
			})), s.trigger("onLoading")
		},
		getViewport: function () {
			var t = s.current && s.current.locked || !1,
				n = {
					x: a.scrollLeft(),
					y: a.scrollTop()
				};
			return t && t.length ? (n.w = t[0].clientWidth, n.h = t[0].clientHeight) : (n.w = d && e.innerWidth ? e.innerWidth : a.width(), n.h = d && e.innerHeight ? e.innerHeight : a.height()), n
		},
		unbindEvents: function () {
			s.wrap && p(s.wrap) && s.wrap.unbind(".fb"), r.unbind(".fb"), a.unbind(".fb")
		},
		bindEvents: function () {
			var e, t = s.current;
			t && (a.bind("orientationchange.fb" + (d ? "" : " resize.fb") + (t.autoCenter && !t.locked ? " scroll.fb" : ""), s.update), e = t.keys, e && r.bind("keydown.fb", function (o) {
				var a = o.which || o.keyCode,
					r = o.target || o.srcElement;
				return 27 === a && s.coming ? !1 : (o.ctrlKey || o.altKey || o.shiftKey || o.metaKey || r && (r.type || n(r).is("[contenteditable]")) || n.each(e, function (e, r) {
					return t.group.length > 1 && r[a] !== i ? (s[e](r[a]), o.preventDefault(), !1) : n.inArray(a, r) > -1 ? (s[e](), o.preventDefault(), !1) : void 0
				}), void 0)
			}), n.fn.mousewheel && t.mouseWheel && s.wrap.bind("mousewheel.fb", function (e, i, o, a) {
				for (var r = e.target || null, l = n(r), c = !1; l.length && !(c || l.is(".fancybox-skin") || l.is(".fancybox-wrap"));) c = u(l[0]), l = n(l).parent();
				0 === i || c || s.group.length > 1 && !t.canShrink && (a > 0 || o > 0 ? s.prev(a > 0 ? "down" : "left") : (0 > a || 0 > o) && s.next(0 > a ? "up" : "right"), e.preventDefault())
			}))
		},
		trigger: function (e, t) {
			var i, o = t || s.coming || s.current;
			if (o) {
				if (n.isFunction(o[e]) && (i = o[e].apply(o, Array.prototype.slice.call(arguments, 1))), i === !1) return !1;
				o.helpers && n.each(o.helpers, function (t, i) {
					i && s.helpers[t] && n.isFunction(s.helpers[t][e]) && s.helpers[t][e](n.extend(!0, {}, s.helpers[t].defaults, i), o)
				})
			}
			r.trigger(e)
		},
		isImage: function (e) {
			return h(e) && e.match(/(^data:image\/.*,)|(\.(jp(e|g|eg)|gif|png|bmp|webp|svg)((\?|#).*)?$)/i)
		},
		isSWF: function (e) {
			return h(e) && e.match(/\.(swf)((\?|#).*)?$/i)
		},
		_start: function (e) {
			var t, i, o, a, r, l = {};
			if (e = g(e), t = s.group[e] || null, !t) return !1;
			if (l = n.extend(!0, {}, s.opts, t), a = l.margin, r = l.padding, "number" === n.type(a) && (l.margin = [a, a, a, a]), "number" === n.type(r) && (l.padding = [r, r, r, r]), l.modal && n.extend(!0, l, {
					closeBtn: !1,
					closeClick: !1,
					nextClick: !1,
					arrows: !1,
					mouseWheel: !1,
					keys: null,
					helpers: {
						overlay: {
							closeClick: !1
						}
					}
				}), l.autoSize && (l.autoWidth = l.autoHeight = !0), "auto" === l.width && (l.autoWidth = !0), "auto" === l.height && (l.autoHeight = !0), l.group = s.group, l.index = e, s.coming = l, !1 === s.trigger("beforeLoad")) return s.coming = null, void 0;
			if (o = l.type, i = l.href, !o) return s.coming = null, s.current && s.router && "jumpto" !== s.router ? (s.current.index = e, s[s.router](s.direction)) : !1;
			if (s.isActive = !0, ("image" === o || "swf" === o) && (l.autoHeight = l.autoWidth = !1, l.scrolling = "visible"), "image" === o && (l.aspectRatio = !0), "iframe" === o && d && (l.scrolling = "scroll"), l.wrap = n(l.tpl.wrap).addClass("fancybox-" + (d ? "mobile" : "desktop") + " fancybox-type-" + o + " fancybox-tmp " + l.wrapCSS).appendTo(l.parent || "body"), n.extend(l, {
					skin: n(".fancybox-skin", l.wrap),
					outer: n(".fancybox-outer", l.wrap),
					inner: n(".fancybox-inner", l.wrap)
				}), n.each(["Top", "Right", "Bottom", "Left"], function (e, t) {
					l.skin.css("padding" + t, m(l.padding[e]))
				}), s.trigger("onReady"), "inline" === o || "html" === o) {
				if (!l.content || !l.content.length) return s._error("content")
			} else if (!i) return s._error("href");
			"image" === o ? s._loadImage() : "ajax" === o ? s._loadAjax() : "iframe" === o ? s._loadIframe() : s._afterLoad()
		},
		_error: function (e) {
			n.extend(s.coming, {
				type: "html",
				autoWidth: !0,
				autoHeight: !0,
				minWidth: 0,
				minHeight: 0,
				scrolling: "no",
				hasError: e,
				content: s.coming.tpl.error
			}), s._afterLoad()
		},
		_loadImage: function () {
			var e = s.imgPreload = new Image;
			e.onload = function () {
				this.onload = this.onerror = null, s.coming.width = this.width / s.opts.pixelRatio, s.coming.height = this.height / s.opts.pixelRatio, s._afterLoad()
			}, e.onerror = function () {
				this.onload = this.onerror = null, s._error("image")
			}, e.src = s.coming.href, e.complete !== !0 && s.showLoading()
		},
		_loadAjax: function () {
			var e = s.coming;
			s.showLoading(), s.ajaxLoad = n.ajax(n.extend({}, e.ajax, {
				url: e.href,
				error: function (e, t) {
					s.coming && "abort" !== t ? s._error("ajax", e) : s.hideLoading()
				},
				success: function (t, n) {
					"success" === n && (e.content = t, s._afterLoad())
				}
			}))
		},
		_loadIframe: function () {
			var e = s.coming,
				t = n(e.tpl.iframe.replace(/\{rnd\}/g, (new Date).getTime())).attr("scrolling", d ? "auto" : e.iframe.scrolling).attr("src", e.href);
			n(e.wrap).bind("onReset", function () {
				try {
					n(this).find("iframe").hide().attr("src", "//about:blank").end().empty()
				} catch (e) {}
			}), e.iframe.preload && (s.showLoading(), t.one("load", function () {
				n(this).data("ready", 1), d || n(this).bind("load.fb", s.update), n(this).parents(".fancybox-wrap").width("100%").removeClass("fancybox-tmp").show(), s._afterLoad()
			})), e.content = t.appendTo(e.inner), e.iframe.preload || s._afterLoad()
		},
		_preloadImages: function () {
			var e, t, n = s.group,
				i = s.current,
				o = n.length,
				a = i.preload ? Math.min(i.preload, o - 1) : 0;
			for (t = 1; a >= t; t += 1) e = n[(i.index + t) % o], "image" === e.type && e.href && ((new Image).src = e.href)
		},
		_afterLoad: function () {
			var e, t, i, o, a, r, l = s.coming,
				c = s.current,
				d = "fancybox-placeholder";
			if (s.hideLoading(), l && s.isActive !== !1) {
				if (!1 === s.trigger("afterLoad", l, c)) return l.wrap.stop(!0).trigger("onReset").remove(), s.coming = null, void 0;
				switch (c && (s.trigger("beforeChange", c), c.wrap.stop(!0).removeClass("fancybox-opened").find(".fancybox-item, .fancybox-nav").remove()), s.unbindEvents(), e = l, t = l.content, i = l.type, o = l.scrolling, n.extend(s, {
					wrap: e.wrap,
					skin: e.skin,
					outer: e.outer,
					inner: e.inner,
					current: e,
					previous: c
				}), a = e.href, i) {
					case "inline":
					case "ajax":
					case "html":
						e.selector ? t = n("<div>").html(t).find(e.selector) : p(t) && (t.data(d) || t.data(d, n('<div class="' + d + '"></div>').insertAfter(t).hide()), t = t.show().detach(), e.wrap.bind("onReset", function () {
							n(this).find(t).length && t.hide().replaceAll(t.data(d)).data(d, !1)
						}));
						break;
					case "image":
						t = e.tpl.image.replace(/\{href\}/g, a);
						break;
					case "swf":
						t = '<object id="fancybox-swf" classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" width="100%" height="100%"><param name="movie" value="' + a + '"></param>', r = "", n.each(e.swf, function (e, n) {
							t += '<param name="' + e + '" value="' + n + '"></param>', r += " " + e + '="' + n + '"'
						}), t += '<embed src="' + a + '" type="application/x-shockwave-flash" width="100%" height="100%"' + r + "></embed></object>"
				}
				p(t) && t.parent().is(e.inner) || e.inner.append(t), s.trigger("beforeShow"), e.inner.css("overflow", "yes" === o ? "scroll" : "no" === o ? "hidden" : o), s._setDimension(), s.reposition(), s.isOpen = !1, s.coming = null, s.bindEvents(), s.isOpened ? c.prevMethod && s.transitions[c.prevMethod]() : n(".fancybox-wrap").not(e.wrap).stop(!0).trigger("onReset").remove(), s.transitions[s.isOpened ? e.nextMethod : e.openMethod](), s._preloadImages()
			}
		},
		_setDimension: function () {
			var e, t, i, o, a, r, l, c, d, p, h, u, y, x, v, w = s.getViewport(),
				b = 0,
				k = !1,
				C = !1,
				W = s.wrap,
				S = s.skin,
				O = s.inner,
				E = s.current,
				T = E.width,
				_ = E.height,
				H = E.minWidth,
				L = E.minHeight,
				P = E.maxWidth,
				R = E.maxHeight,
				j = E.scrolling,
				M = E.scrollOutside ? E.scrollbarWidth : 0,
				A = E.margin,
				I = g(A[1] + A[3]),
				D = g(A[0] + A[2]);
			if (W.add(S).add(O).width("auto").height("auto").removeClass("fancybox-tmp"), e = g(S.outerWidth(!0) - S.width()), t = g(S.outerHeight(!0) - S.height()), i = I + e, o = D + t, a = f(T) ? (w.w - i) * g(T) / 100 : T, r = f(_) ? (w.h - o) * g(_) / 100 : _, "iframe" === E.type) {
				if (x = E.content, E.autoHeight && 1 === x.data("ready")) try {
					x[0].contentWindow.document.location && (O.width(a).height(9999), v = x.contents().find("body"), M && v.css("overflow-x", "hidden"), r = v.outerHeight(!0))
				} catch (V) {}
			} else(E.autoWidth || E.autoHeight) && (O.addClass("fancybox-tmp"), E.autoWidth || O.width(a), E.autoHeight || O.height(r), E.autoWidth && (a = O.width()), E.autoHeight && (r = O.height()), O.removeClass("fancybox-tmp"));
			if (T = g(a), _ = g(r), d = a / r, H = g(f(H) ? g(H, "w") - i : H), P = g(f(P) ? g(P, "w") - i : P), L = g(f(L) ? g(L, "h") - o : L), R = g(f(R) ? g(R, "h") - o : R), l = P, c = R, E.fitToView && (P = Math.min(w.w - i, P), R = Math.min(w.h - o, R)), u = w.w - I, y = w.h - D, E.aspectRatio ? (T > P && (T = P, _ = g(T / d)), _ > R && (_ = R, T = g(_ * d)), H > T && (T = H, _ = g(T / d)), L > _ && (_ = L, T = g(_ * d))) : (T = Math.max(H, Math.min(T, P)), E.autoHeight && "iframe" !== E.type && (O.width(T), _ = O.height()), _ = Math.max(L, Math.min(_, R))), E.fitToView)
				if (O.width(T).height(_), W.width(T + e), p = W.width(), h = W.height(), E.aspectRatio)
					for (;
						(p > u || h > y) && T > H && _ > L && !(b++ > 19);) _ = Math.max(L, Math.min(R, _ - 10)), T = g(_ * d), H > T && (T = H, _ = g(T / d)), T > P && (T = P, _ = g(T / d)), O.width(T).height(_), W.width(T + e), p = W.width(), h = W.height();
				else T = Math.max(H, Math.min(T, T - (p - u))), _ = Math.max(L, Math.min(_, _ - (h - y)));
			M && "auto" === j && r > _ && u > T + e + M && (T += M), O.width(T).height(_), W.width(T + e), p = W.width(), h = W.height(), k = (p > u || h > y) && T > H && _ > L, C = E.aspectRatio ? l > T && c > _ && a > T && r > _ : (l > T || c > _) && (a > T || r > _), n.extend(E, {
				dim: {
					width: m(p),
					height: m(h)
				},
				origWidth: a,
				origHeight: r,
				canShrink: k,
				canExpand: C,
				wPadding: e,
				hPadding: t,
				wrapSpace: h - S.outerHeight(!0),
				skinSpace: S.height() - _
			}), !x && E.autoHeight && _ > L && R > _ && !C && O.height("auto")
		},
		_getPosition: function (e) {
			var t = s.current,
				n = s.getViewport(),
				i = t.margin,
				o = s.wrap.width() + i[1] + i[3],
				a = s.wrap.height() + i[0] + i[2],
				r = {
					position: "absolute",
					top: i[0],
					left: i[3]
				};
			return t.autoCenter && t.fixed && !e && a <= n.h && o <= n.w ? r.position = "fixed" : t.locked || (r.top += n.y, r.left += n.x), r.top = m(Math.max(r.top, r.top + (n.h - a) * t.topRatio)), r.left = m(Math.max(r.left, r.left + (n.w - o) * t.leftRatio)), r
		},
		_afterZoomIn: function () {
			var e = s.current;
			e && (s.isOpen = s.isOpened = !0, s.wrap.css("overflow", "visible").addClass("fancybox-opened"), s.update(), (e.closeClick || e.nextClick && s.group.length > 1) && s.inner.css("cursor", "pointer").bind("click.fb", function (t) {
				n(t.target).is("a") || n(t.target).parent().is("a") || (t.preventDefault(), s[e.closeClick ? "close" : "next"]())
			}), e.closeBtn && n(e.tpl.closeBtn).appendTo(s.skin).bind("click.fb", function (e) {
				e.preventDefault(), s.close()
			}), e.arrows && s.group.length > 1 && ((e.loop || e.index > 0) && n(e.tpl.prev).appendTo(s.outer).bind("click.fb", s.prev), (e.loop || e.index < s.group.length - 1) && n(e.tpl.next).appendTo(s.outer).bind("click.fb", s.next)), s.trigger("afterShow"), e.loop || e.index !== e.group.length - 1 ? s.opts.autoPlay && !s.player.isActive && (s.opts.autoPlay = !1, s.play()) : s.play(!1))
		},
		_afterZoomOut: function (e) {
			e = e || s.current, n(".fancybox-wrap").trigger("onReset").remove(), n.extend(s, {
				group: {},
				opts: {},
				router: !1,
				current: null,
				isActive: !1,
				isOpened: !1,
				isOpen: !1,
				isClosing: !1,
				wrap: null,
				skin: null,
				outer: null,
				inner: null
			}), s.trigger("afterClose", e)
		}
	}), s.transitions = {
		getOrigPosition: function () {
			var e = s.current,
				t = e.element,
				n = e.orig,
				i = {},
				o = 50,
				a = 50,
				r = e.hPadding,
				l = e.wPadding,
				c = s.getViewport();
			return !n && e.isDom && t.is(":visible") && (n = t.find("img:first"), n.length || (n = t)), p(n) ? (i = n.offset(), n.is("img") && (o = n.outerWidth(), a = n.outerHeight())) : (i.top = c.y + (c.h - a) * e.topRatio, i.left = c.x + (c.w - o) * e.leftRatio), ("fixed" === s.wrap.css("position") || e.locked) && (i.top -= c.y, i.left -= c.x), i = {
				top: m(i.top - r * e.topRatio),
				left: m(i.left - l * e.leftRatio),
				width: m(o + l),
				height: m(a + r)
			}
		},
		step: function (e, t) {
			var n, i, o, a = t.prop,
				r = s.current,
				l = r.wrapSpace,
				c = r.skinSpace;
			("width" === a || "height" === a) && (n = t.end === t.start ? 1 : (e - t.start) / (t.end - t.start), s.isClosing && (n = 1 - n), i = "width" === a ? r.wPadding : r.hPadding, o = e - i, s.skin[a](g("width" === a ? o : o - l * n)), s.inner[a](g("width" === a ? o : o - l * n - c * n)))
		},
		zoomIn: function () {
			var e = s.current,
				t = e.pos,
				i = e.openEffect,
				o = "elastic" === i,
				a = n.extend({
					opacity: 1
				}, t);
			delete a.position, o ? (t = this.getOrigPosition(), e.openOpacity && (t.opacity = .1)) : "fade" === i && (t.opacity = .1), s.wrap.css(t).animate(a, {
				duration: "none" === i ? 0 : e.openSpeed,
				easing: e.openEasing,
				step: o ? this.step : null,
				complete: s._afterZoomIn
			})
		},
		zoomOut: function () {
			var e = s.current,
				t = e.closeEffect,
				n = "elastic" === t,
				i = {
					opacity: .1
				};
			n && (i = this.getOrigPosition(), e.closeOpacity && (i.opacity = .1)), s.wrap.animate(i, {
				duration: "none" === t ? 0 : e.closeSpeed,
				easing: e.closeEasing,
				step: n ? this.step : null,
				complete: s._afterZoomOut
			})
		},
		changeIn: function () {
			var e, t = s.current,
				n = t.nextEffect,
				i = t.pos,
				o = {
					opacity: 1
				},
				a = s.direction,
				r = 200;
			i.opacity = .1, "elastic" === n && (e = "down" === a || "up" === a ? "top" : "left", "down" === a || "right" === a ? (i[e] = m(g(i[e]) - r), o[e] = "+=" + r + "px") : (i[e] = m(g(i[e]) + r), o[e] = "-=" + r + "px")), "none" === n ? s._afterZoomIn() : s.wrap.css(i).animate(o, {
				duration: t.nextSpeed,
				easing: t.nextEasing,
				complete: s._afterZoomIn
			})
		},
		changeOut: function () {
			var e = s.previous,
				t = e.prevEffect,
				i = {
					opacity: .1
				},
				o = s.direction,
				a = 200;
			"elastic" === t && (i["down" === o || "up" === o ? "top" : "left"] = ("up" === o || "left" === o ? "-" : "+") + "=" + a + "px"), e.wrap.animate(i, {
				duration: "none" === t ? 0 : e.prevSpeed,
				easing: e.prevEasing,
				complete: function () {
					n(this).trigger("onReset").remove()
				}
			})
		}
	}, s.helpers.overlay = {
		defaults: {
			closeClick: !0,
			speedOut: 200,
			showEarly: !0,
			css: {},
			locked: !d,
			fixed: !0
		},
		overlay: null,
		fixed: !1,
		el: n("html"),
		create: function (e) {
			var t;
			e = n.extend({}, this.defaults, e), this.overlay && this.close(), t = s.coming ? s.coming.parent : e.parent, this.overlay = n('<div class="fancybox-overlay"></div>').appendTo(t && t.lenth ? t : "body"), this.fixed = !1, e.fixed && s.defaults.fixed && (this.overlay.addClass("fancybox-overlay-fixed"), this.fixed = !0)
		},
		open: function (e) {
			var t = this;
			e = n.extend({}, this.defaults, e), this.overlay ? this.overlay.unbind(".overlay").width("auto").height("auto") : this.create(e), this.fixed || (a.bind("resize.overlay", n.proxy(this.update, this)), this.update()), e.closeClick && this.overlay.bind("click.overlay", function (e) {
				return n(e.target).hasClass("fancybox-overlay") ? (s.isActive ? s.close() : t.close(), !1) : void 0
			}), this.overlay.css(e.css).show()
		},
		close: function () {
			a.unbind("resize.overlay"), this.el.hasClass("fancybox-lock") && (n(".fancybox-margin").removeClass("fancybox-margin"), this.el.removeClass("fancybox-lock"), a.scrollTop(this.scrollV).scrollLeft(this.scrollH)), n(".fancybox-overlay").remove().hide(), n.extend(this, {
				overlay: null,
				fixed: !1
			})
		},
		update: function () {
			var e, n = "100%";
			this.overlay.width(n).height("100%"), l ? (e = Math.max(t.documentElement.offsetWidth, t.body.offsetWidth), r.width() > e && (n = r.width())) : r.width() > a.width() && (n = r.width()), this.overlay.width(n).height(r.height())
		},
		onReady: function (e, t) {
			var i = this.overlay;
			n(".fancybox-overlay").stop(!0, !0), i || this.create(e), e.locked && this.fixed && t.fixed && (t.locked = this.overlay.append(t.wrap), t.fixed = !1), e.showEarly === !0 && this.beforeShow.apply(this, arguments)
		},
		beforeShow: function (e, t) {
			t.locked && !this.el.hasClass("fancybox-lock") && (this.fixPosition !== !1 && n("*").filter(function () {
				return "fixed" === n(this).css("position") && !n(this).hasClass("fancybox-overlay") && !n(this).hasClass("fancybox-wrap")
			}).addClass("fancybox-margin"), this.el.addClass("fancybox-margin"), this.scrollV = a.scrollTop(), this.scrollH = a.scrollLeft(), this.el.addClass("fancybox-lock"), a.scrollTop(this.scrollV).scrollLeft(this.scrollH)), this.open(e)
		},
		onUpdate: function () {
			this.fixed || this.update()
		},
		afterClose: function (e) {
			this.overlay && !s.coming && this.overlay.fadeOut(e.speedOut, n.proxy(this.close, this))
		}
	}, s.helpers.title = {
		defaults: {
			type: "float",
			position: "bottom"
		},
		beforeShow: function (e) {
			var t, i, o = s.current,
				a = o.title,
				r = e.type;
			if (n.isFunction(a) && (a = a.call(o.element, o)), h(a) && "" !== n.trim(a)) {
				switch (t = n('<div class="fancybox-title fancybox-title-' + r + '-wrap">' + a + "</div>"), r) {
					case "inside":
						i = s.skin;
						break;
					case "outside":
						i = s.wrap;
						break;
					case "over":
						i = s.inner;
						break;
					default:
						i = s.skin, t.appendTo("body"), l && t.width(t.width()), t.wrapInner('<span class="child"></span>'), s.current.margin[2] += Math.abs(g(t.css("margin-bottom")))
				}
				t["top" === e.position ? "prependTo" : "appendTo"](i)
			}
		}
	}, n.fn.fancybox = function (e) {
		var t, i = n(this),
			o = this.selector || "",
			a = function (a) {
				var r, l, c = n(this).blur(),
					d = t;
				a.ctrlKey || a.altKey || a.shiftKey || a.metaKey || c.is(".fancybox-wrap") || (r = e.groupAttr || "data-fancybox-group", l = c.attr(r), l || (r = "rel", l = c.get(0)[r]), l && "" !== l && "nofollow" !== l && (c = o.length ? n(o) : i, c = c.filter("[" + r + '="' + l + '"]'), d = c.index(this)), e.index = d, s.open(c, e) !== !1 && a.preventDefault())
			};
		return e = e || {}, t = e.index || 0, o && e.live !== !1 ? r.undelegate(o, "click.fb-start").delegate(o + ":not('.fancybox-item, .fancybox-nav')", "click.fb-start", a) : i.unbind("click.fb-start").bind("click.fb-start", a), this.filter("[data-fancybox-start=1]").trigger("click"), this
	}, r.ready(function () {
		var t, a;
		n.scrollbarWidth === i && (n.scrollbarWidth = function () {
			var e = n('<div style="width:50px;height:50px;overflow:auto"><div/></div>').appendTo("body"),
				t = e.children(),
				i = t.innerWidth() - t.height(99).innerWidth();
			return e.remove(), i
		}), n.support.fixedPosition === i && (n.support.fixedPosition = function () {
			var e = n('<div style="position:fixed;top:20px;"></div>').appendTo("body"),
				t = 20 === e[0].offsetTop || 15 === e[0].offsetTop;
			return e.remove(), t
		}()), n.extend(s.defaults, {
			scrollbarWidth: n.scrollbarWidth(),
			fixed: n.support.fixedPosition,
			parent: n("body")
		}), t = n(e).width(), o.addClass("fancybox-lock-test"), a = n(e).width(), o.removeClass("fancybox-lock-test"), n("<style type='text/css'>.fancybox-margin{margin-right:" + (a - t) + "px;}</style>").appendTo("head")
	})
}(window, document, jQuery);

$(document).ready(function(){
    $('.latest-videos').slick({
        slidesToShow: 4,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 1500,
        arrows: false,
        dots: false,
        pauseOnHover: false,
        responsive: [{
            breakpoint: 768,
            settings: {
                slidesToShow: 2
            }
        }, {
            breakpoint: 520,
            settings: {
                slidesToShow: 1
            }
        }]
    });
});
