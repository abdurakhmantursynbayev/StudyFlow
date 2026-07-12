import { createContext, useContext, useEffect, useState } from "react";

type AuthContextType = {
    token: string | null;
    login: (token: string) => void;
    logout: () => void;
};

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: React.ReactNode }) {
    const [token, setToken] = useState<string | null>(null);

    useEffect(() => {
        const savedToken = localStorage.getItem("access_token");

        if (savedToken) {
            setToken(savedToken);
        }
    }, []);

    function login(token: string) {
        localStorage.setItem("access_token", token);
        setToken(token);
    }

    function logout() {
        localStorage.removeItem("access_token");
        setToken(null);
    }

    return (
        <AuthContext.Provider value={{ token, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
}

export function useAuth() {
    const context = useContext(AuthContext);

    if (!context) {
        throw new Error("useAuth must be used inside AuthProvider");
    }

    return context;
}