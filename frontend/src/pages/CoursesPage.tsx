import { useEffect, useState } from "react";
import api from "../api/client";

type Course = {
    id: number;
    title: string;
    description: string;
};

export default function CoursesPage() {
    const [courses, setCourses] = useState<Course[]>([]);

    useEffect(() => {
        async function loadCourses() {
            try {
                const response = await api.get("/courses");
                setCourses(response.data);
            } catch (error) {
                console.error(error);
            }
        }

        loadCourses();
    }, []);

    return (
        <main className="hero">
            <h1>Courses</h1>

            <div className="courses-list">
                {courses.map((course) => (
                    <div key={course.id} className="course-card">
                        <h2>{course.title}</h2>

                        <p>{course.description}</p>
                    </div>
                ))}
            </div>
        </main>
    );
}