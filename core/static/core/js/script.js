(function ($) {

	'use strict';
	var countDownDate = new Date("April 15, 2021 00:00:00").getTime();
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
