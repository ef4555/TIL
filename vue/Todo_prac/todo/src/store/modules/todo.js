const todos = {
  namespaced: true,

  state: {
      list: [
        // 개별 todo Object
        {
          id: 1638771553377,                // nowDateObj.getTime()
          content: 'Vue',                   // Todo 내용
          dueDateTime: '2021-12-09T00:00',  // 마감일
          isCompleted: false,               // 완료된 할 일
          isImportant: true,				        // 중요 할 일
        },
        {
          id: 1638771553378,
          content: 'Vue Router',
          dueDateTime: '2021-12-10T00:00',
          isCompleted: false,
          isImportant: true,
        },
        {
          id: 16387715533779,
          content: 'Vuex',
          dueDateTime: '2021-12-11T00:00',
          isCompleted: true,
          isImportant: false,
        },
      ],
  },
  mutations: {
    CREATE_TODO(state, data) {
      const dueDateTime = new Date()
      const year = dueDateTime.getFullYear();
      const month = String(dueDateTime.getMonth() + 1).padStart(2, '0');
      const day = String(dueDateTime.getDate()).padStart(2, '0');
      const hours = String(dueDateTime.getHours()).padStart(2, '0');
      const minutes = String(dueDateTime.getMinutes()).padStart(2, '0');
      const aaa = `${year}-${month}-${day}T${hours}:${minutes}`;

      state.list.push({'id': dueDateTime.getTime(), 'content': data, 'dueDateTime': aaa, 'isCompleted': false, 'isImportant': false,})
    }
  },
  actions: {
    createTodo(context, data) {
      context.commit('CREATE_TODO', data)
    }
  },
}

export default todos