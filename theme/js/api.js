import $ from 'jquery'

function set_api_menu_active(href) {
  $('li.active').removeClass('active');
  $(`a[href="${href}"]`).parents('.tab-container').addClass('active');
}

function change_menu_tab() {
  if (window.location.hash) {
    set_api_menu_active(window.location.hash);
  } else {
    set_api_menu_active('#introduction');
  }
}

function set_code_syntax() {
  $(document).ready(() => {
    document.querySelectorAll('div code').forEach((block) => {
      hljs.highlightBlock(block);
    });
  });
}

if (window.jQuery) {
  change_menu_tab();

  $(window).bind('hashchange', () => {
    change_menu_tab();
  });

  set_code_syntax();
}
