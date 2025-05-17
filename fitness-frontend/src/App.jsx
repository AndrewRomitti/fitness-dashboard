import './App.css'
import WorkoutForm from './components/WorkoutForm';

function App() {
  return (
    <div className="min-h-screen bg-gray-100 text-gray-800">
      <header className="bg-white shadow p-4">
        <h1 className="text-2xl font-bold text-blue-600">Fitness Dashboard</h1>
      </header>

      <main className="p-6">
        <WorkoutForm />
      </main>
    </div>
  )
}

export default App
