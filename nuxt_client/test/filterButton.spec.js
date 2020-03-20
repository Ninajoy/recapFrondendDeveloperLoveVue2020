import { mount } from '@vue/test-utils'
import filterThemes from '@/components/filterThemes.vue'

describe('filterThemes', () => {
  const wrapper = mount(filterThemes, {
    propsData: {
      theme : {
        value: 'Vue'
      }
    }
  })

  test('has an element with the class filter-button', () => {
    expect(wrapper.classes('filter-button')).toBe(true)
  })

  test('has an element with the data-theme attribute', () => {
    expect(wrapper.contains('[data-theme]')).toBe(true)
  })

  test('the data-theme attribute has the value of the theme props', () => {
    expect(wrapper.attributes()['data-filter']).toBe('Vue')
    // expect(wrapper.props('theme')).toBe('Vue')
  })
})
