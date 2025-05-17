import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  return (
    <div className="min-h-screen bg-gray-100 text-gray-800">
      <header className="bg-white shadow p-4">
        <h1 className="text-2xl font-bold text-blue-600">Fitness Dashboard</h1>
      </header>

      <main className="p-6">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <section className="bg-white rounded-2xl p-4 shadow">
            <h2 className="text-xl font-semibold mb-2">Workouts</h2>
          </section>
          <section className="bg-white rounded-2xl p-4 shadow">
            <h2 className="text-xl font-semibold mb-2">Calories</h2>
          </section>
        </div>
      </main>
    </div>
  )
}

export default App
