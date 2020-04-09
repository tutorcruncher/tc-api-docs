import $ from 'jquery'

function set_menu_heading_active(href) {
  $('.active-subheading').removeClass('active-subheading')
  $('li.active').removeClass('active')

  const $subheading = $(`a[href="${href}"]`)
  $subheading.addClass('active-subheading')
  $subheading.parents('.tab-container').addClass('active')
}

function scroll_to_menu_active_heading() {
  const $menu_tabs = $('.menu-bar-tabs')
  $menu_tabs.scrollTop($menu_tabs.scrollTop() + $('.tab-container.active').position().top - 50)
}

function change_menu_tab(update_menu_scroll=true) {
  if (window.location.hash) {
    set_menu_heading_active(window.location.hash)
  } else {
    set_menu_heading_active('#introduction')
    update_menu_scroll = false
  }
  if (update_menu_scroll) {
    scroll_to_menu_active_heading()
  }
}

function init_change_menu_tab() {
  change_menu_tab()
  $(window).bind('hashchange', () => {
    change_menu_tab()
  })
}

function _toggle(translate_amount, item_to_show, item_to_hide) {
  const $menu_bar_con = $('.api-menu-bar-container')

  $menu_bar_con.css('transform', `translateX(${translate_amount}px)`)
  item_to_show.show()
  item_to_hide.hide()
}

function init_menu_toggle() {
  const $show = $('#show-menu')
  const $hide = $('#hide-menu')

  $show.click(() => {
    _toggle(0, $hide, $show)
  })

  $hide.click(() => {
    _toggle(-230, $show, $hide)
  })

  $(window).resize(() => {
    if ($(window).width() > 767) {
      _toggle(0, $show, $hide)
    } else {
      _toggle(-230, $show, $hide)
    }
  })
}

function init_set_code_syntax() {
  $(document).ready(() => {
    document.querySelectorAll('.api-example-container code').forEach((block) => {
      hljs.highlightBlock(block)
    })
  })
}

function init_scroll_heading_change() {
  let current_hash = window.location.hash
  $('body').scroll(() => {
    $('.api-section-heading, .api-subsection').each((i, el) => {
      const $el = $(el)
      const top = window.pageYOffset
      const distance = top - $el.position().top
      const hash = $el.attr('id')
      const padding = 30
      if (hash && current_hash !== hash && distance < padding && distance > -padding) {
        window.history.pushState(null, null, `#${hash}`)
        current_hash = hash
        change_menu_tab()
      }
    })
  })
}

function init_attribute_children_dropdown () {
  $('.attribute-children-heading').click((e) => {
    const $container = $(e.target).parent()
    const active_class = 'attribute-active'
    if ($container.hasClass(active_class)) {
      $container.removeClass(active_class)
    } else {
      $container.addClass(active_class)
    }
  })
}

function get_release_info () {
  $.get('http://localhost:3000/system.txt').done((r) => {
    const version = /VERSION\: (.*)\n/.exec(r)[1]
    const dt = /DATE\: (.*)T/.exec(r)[1]
    $('#release-info').text(`${version} (${dt})`)
  })
}

if (window.jQuery) {
  init_menu_toggle()
  init_change_menu_tab()
  init_scroll_heading_change()
  init_set_code_syntax()
  init_attribute_children_dropdown()
  get_release_info()
}
