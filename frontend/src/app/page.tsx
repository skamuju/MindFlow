import Image from 'next/image';
import top from '../../public/assets/top_flow.png';
import bottom from '../../public/assets/bottom_flow.png';
import styles from "./page.module.css";

export default function Home() {
  return (
    <div className={styles.main}>
      <Image src={top} alt="Top Flow" className={styles.top_flow}/>
      <div className={styles.header}>
        <h1>mindflow</h1>
        <h2>a journaling app to help understand yourself</h2>
      </div>
      <Image src={bottom} alt="Bottom Flow" className={styles.bottom_flow}/>
    </div>
  );
}
