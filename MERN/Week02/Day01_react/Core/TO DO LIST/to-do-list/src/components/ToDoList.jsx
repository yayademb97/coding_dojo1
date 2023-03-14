import React, { useEffect, useState } from 'react'
import uuid from 'react-uuid';
import './ToDoList.css';

const ToDoList = () => {
    const [input, setInput] = useState('');
    const [tasks, setTasks] = useState([]);

    // Add Task
    const submitHandler = (e) => {
        e.preventDefault();
        setTasks([...tasks, { input, id: new Date().getTime().toString(), isDone: false }]);

        // Clear Input
        setInput('');
    }

    // Delete Task
    const deleteTask = (id) => {
        setTasks(tasks.filter(item => item.id !== id))
    }

    return <div className='main'>
        <div className="form">
            <form onSubmit={submitHandler} >
                <input type="text" placeholder="Add task" value={input} onChange={e => setInput(e.target.value)} />
                <input type="submit" value='Add' />
            </form>
        </div>

        <div className='tasks'>
            {tasks.map(task => {
                return <div key={task.id} className="task">
                    <p>{task.input}</p>
                    <input type="checkbox" name="" id="" />
                    <button onClick={() => deleteTask(task.id)}>Delete</button>
                </div>
            })}
        </div>
    </div>
}

export default ToDoList;