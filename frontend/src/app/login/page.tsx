import Image from "next/image";
import login_top from "../../../public/assets/login_top.png";
import login_bottom from "../../../public/assets/login_bottom.png";
import styles from "./page.module.css";

export default function Login() {
  return (
    <div className={styles.main}>
      <Image src={login_top} alt="Top Flow" className={styles.top_flow} />
      <div className={styles.message}>
        <h1>mindflow</h1>
        <button className={styles.login_button}>sign up</button>
        <button className={styles.login_button}>login</button>
      </div>
      <Image
        src={login_bottom}
        alt="Bottom Flow"
        className={styles.bottom_flow}
      />
    </div>
  );
}
