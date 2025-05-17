import { useEffect, useState } from "react";

export default function WorkoutsList() {
    const [workouts, setWorkouts] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetch("http://localhost:5000/workouts")
            .then((res) => {
                if (!res.ok) throw new Error("Failed to fetch workouts");
                return res.json();
            })
            .then((data) => {
                setWorkouts(data);
                setLoading(false);
            })
            .catch((err) => {
                setError(err.message);
                setLoading(false);
            });
    }, []);

    if (loading) return <p>Loading workouts...</p>;
    if (error) return <p>Error: {error}</p>;

    return (
        <div>
            <h2 className="text-xl font-semibold mb-4">Workouts</h2>
            <ul>
                {workouts.map((w) => (
                    <li key={w.id} className="mb-2 p-2 border rounded">
                        <strong>{w.type}</strong> on {w.date} for {w.duration_min}
                    </li>
                ))}
            </ul>
        </div>
    )
}