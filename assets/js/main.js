/* Work Beyond Borders — site behaviour */
(function () {
  'use strict';

  var root = document.documentElement;

  /* ---------- header: solid once scrolled past the hero top ---------- */
  var header = document.querySelector('.site-header');
  if (header) {
    var onScroll = function () {
      header.classList.toggle('is-stuck', window.scrollY > 40);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---------- mobile nav ---------- */
  var toggle = document.querySelector('.nav-toggle');
  if (toggle) {
    toggle.addEventListener('click', function () {
      var open = root.classList.toggle('nav-open');
      toggle.setAttribute('aria-expanded', String(open));
    });
    document.querySelectorAll('.nav a').forEach(function (a) {
      a.addEventListener('click', function () {
        root.classList.remove('nav-open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* ---------- reveal on scroll ---------- */
  var targets = document.querySelectorAll('.reveal');
  if (targets.length) {
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) {
            e.target.classList.add('is-in');
            io.unobserve(e.target);
          }
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
      targets.forEach(function (t) { io.observe(t); });
    } else {
      targets.forEach(function (t) { t.classList.add('is-in'); });
    }
  }

  /* ---------- careers accordion ---------- */
  var roles = document.querySelectorAll('.role');
  roles.forEach(function (role) {
    var btn = role.querySelector('.role__btn');
    var panel = role.querySelector('.role__panel');
    if (!btn || !panel) return;

    btn.addEventListener('click', function () {
      var willOpen = !role.classList.contains('is-open');
      roles.forEach(function (other) {
        other.classList.remove('is-open');
        var b = other.querySelector('.role__btn');
        var p = other.querySelector('.role__panel');
        if (b) b.setAttribute('aria-expanded', 'false');
        if (p) p.setAttribute('aria-hidden', 'true');
      });
      if (willOpen) {
        role.classList.add('is-open');
        btn.setAttribute('aria-expanded', 'true');
        panel.setAttribute('aria-hidden', 'false');
      }
    });
  });

  /* ---------- photo rails ---------- */
  document.querySelectorAll('.rail').forEach(function (rail) {
    var track = rail.querySelector('.rail__track');
    if (!track) return;

    var step = function () {
      var first = track.querySelector('img');
      return first ? first.getBoundingClientRect().width + 14 : 240;
    };

    rail.querySelectorAll('.rail__btn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var dir = btn.classList.contains('rail__btn--prev') ? -1 : 1;
        track.scrollBy({ left: dir * step() * 2, behavior: 'smooth' });
      });
    });

    var sync = function () {
      var max = track.scrollWidth - track.clientWidth - 2;
      var prev = rail.querySelector('.rail__btn--prev');
      var next = rail.querySelector('.rail__btn--next');
      if (prev) prev.style.opacity = track.scrollLeft <= 2 ? '.35' : '1';
      if (next) next.style.opacity = track.scrollLeft >= max ? '.35' : '1';
    };
    sync();
    track.addEventListener('scroll', sync, { passive: true });
    window.addEventListener('resize', sync);
  });

})();
