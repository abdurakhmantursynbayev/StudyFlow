export default function RegisterPage() {
    return (
        <main className="auth-page">
            <div className="auth-card">
                <h1>Create Account</h1>

                <form>
                    <input
                        type="text"
                        placeholder="Username"
                    />

                    <input
                        type="text"
                        placeholder="Full Name"
                    />

                    <input
                        type="password"
                        placeholder="Password"
                    />

                    <select defaultValue="STUDENT">
                        <option value="STUDENT">Student</option>
                        <option value="TEACHER">Teacher</option>
                    </select>

                    <button type="submit">
                        Register
                    </button>
                </form>
            </div>
        </main>
    );
}