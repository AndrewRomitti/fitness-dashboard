import { useState } from 'react';

export default function WorkoutForm() {
    const [type, setType] = useState('');
    const [duration, setDuration] = useState('');
    const [date, setDate] = useState('');
    const [message, setMessage] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();

        const workoutData = { type, duration, date};

            try {
                const res = await fetch('http://localhost:5000/api/workouts', {
                    method:'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify( {date, type, duration_min: Number(duration)}),
                });

                if (res.ok) {
                    setMessage('Workout logged successfully');
                    setType('');
                    setDuration('');
                    setDate('');
                } else {
                    setMessage('Failed to log workout');
                } 
            } catch (error) {
                setMessage('Error: '+ error.message);
            }
    }



    return (
        <form onSubmit={handleSubmit} className="bg-white p-4 rounded shadow max-w-md">
            <h3 className="text-lg font-semibold mb-4">Log a Workout</h3>

            <label className="block mb-2">
                Workout Type
                <input
                    type="text"
                    value={type}
                    onChange={(e) => setType(e.target.value)}
                    required
                    className="w-full border rounded px-3 py-2 mt-1"
                    />
            </label>

            <label className="block mb-2">
                Duration (minutes)
                <input
                    type="number"
                    value={duration}
                    onChange={(e) => setDuration(e.target.value)}
                    required
                    min="1"
                    className="w-full border rounded px-3 py-2 mt-1"
                    />
            </label>

            <label className="block mb-4">
                Date
                <input
                    type="date"
                    value={date}
                    onChange={(e) => setDate(e.target.value)}
                    required
                    className="w-full border rounded px-3 py-2 mt-1"
                    />
            </label>

            <button
                type="submit"
                className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
            >Submit</button>

            {message && <p className="mt-4 text-sm text-gray-700">{message}</p>}
        </form>
    )


}