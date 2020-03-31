import $ from 'jquery'

function set_api_menu_active(href) {
  $('.active-subheading').removeClass('active-subheading');
  $('li.active').removeClass('active');
  const $subheading = $(`a[href="${href}"]`);
  $subheading.addClass('active-subheading');
  $subheading.parents('.tab-container').addClass('active');
}

function change_menu_tab() {
  if (window.location.hash) {
    set_api_menu_active(window.location.hash);
  } else {
    window.location.hash = '#introduction';
    set_api_menu_active('#introduction');
  }
}

function set_code_syntax() {
  $(document).ready(() => {
    document.querySelectorAll('.api-example-container code').forEach((block) => {
      hljs.highlightBlock(block);
    });
  });
}

function _toggle(translate_amount, item_to_show, item_to_hide) {
  const $menu_bar_con = $('.api-menu-bar-container');

  $menu_bar_con.css('transform', `translateX(${translate_amount}px)`);
  item_to_show.show();
  item_to_hide.hide();
}

function menu_toggle() {
  const $show = $('#show-menu');
  const $hide = $('#hide-menu');

  $show.click(() => {
    _toggle(0, $hide, $show)
  });

  $hide.click(() => {
    _toggle(-230, $show, $hide)
  });

  $(window).resize(() => {
    if ($(window).width() > 767) {
      _toggle(0, $show, $hide)
    } else {
      _toggle(-230, $show, $hide)
    }
  });
}

function scroll_heading_change() {
  let current_hash = window.location.hash;
  $('body').scroll(() => {
    $('.api-section-heading, .api-subsection').each((i, el) => {
      const $el = $(el);
      const top = window.pageYOffset;
      const distance = top - $el.position().top;
      const hash = $el.attr('id');
      const padding = 30;
      if (hash && current_hash !== hash && distance < padding && distance > -padding) {
        window.history.pushState(null, null, `#${hash}`);
        current_hash = hash;
        change_menu_tab();
      }
    });
  });
}

if (window.jQuery) {
  menu_toggle();
  change_menu_tab();
  scroll_heading_change();

  $(window).bind('hashchange', () => {
    change_menu_tab();
  });

  set_code_syntax();
}
