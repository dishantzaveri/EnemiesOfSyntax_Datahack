import * as THREE from "three";
import { useMemo } from "react";
import { Suspense } from "react";
import { Canvas, applyProps } from "@react-three/fiber";
import {
  useGLTF,
  ContactShadows,
  OrbitControls,
  Environment,
} from "@react-three/drei";
import { FlakesTexture } from "three-stdlib";
import { Model } from "./Model";

export default function Car() {
  return (
    <Suspense fallback={null}>
      <Canvas shadows dpr={[1, 2]} camera={{ position: [-7.5, -7.5, -7.5] }}>
        {/*<Lamborghini scale={0.015} />*/}
        <Model />
        <spotLight
          position={[0, 30, 0]}
          angle={0.25}
          penumbra={1}
          intensity={6}
          shadow-bias={-0.0001}
        />
        <ambientLight intensity={1.2} />

        {/* We're building a cube-mapped environment declaratively.
          Anything you put in here will be filmed (once) by a cubemap-camera
          and applied to the scenes environment, and optionally background. */}

        <OrbitControls
          enablePan={false}
          enableZoom={true}
          autoRotate={true}
          minPolarAngle={Math.PI / 2.4}
          maxPolarAngle={Math.PI / 2.4}
        />
      </Canvas>
    </Suspense>
  );
}

/*
Author: Steven Grey (https://sketchfab.com/Steven007)
License: CC-BY-NC-4.0 (http://creativecommons.org/licenses/by-nc/4.0/)
Source: https://sketchfab.com/3d-models/lamborghini-urus-2650599973b649ddb4460ff6c03e4aa2
Title: Lamborghini Urus
*/
function Lamborghini(props) {
  const { scene, nodes, materials } = useGLTF("./lambo.glb");

  useMemo(() => {
    Object.values(nodes).forEach((node) => {
      if (node.isMesh) {
        // Set up shadows
        node.receiveShadow = node.castShadow = true;
        // Fix glas, normals look messed up in the original
        if (node.name.startsWith("glass")) node.geometry.computeVertexNormals();
        // Fix logo, too dark
        if (node.name === "silver_001_BreakDiscs_0")
          node.material = applyProps(materials.BreakDiscs.clone(), {
            color: "#ddd",
          });
      }
    });
    // Fix windows, they have to be inset some more
    nodes["glass_003"].scale.setScalar(2.7);
    // Fix inner frame, too light
    applyProps(materials.FrameBlack, {
      metalness: 0.5,
      roughness: 1,
      color: "black",
    });
    // Wheels, change color from chrome to black matte
    applyProps(materials.Chrome, {
      metalness: 1,
      roughness: 0.2,
      color: "#333",
    });
    applyProps(materials.BreakDiscs, {
      metalness: 0.2,
      roughness: 0.2,
      color: "#555",
    });
    applyProps(materials.TiresGum, { metalness: 0, color: "#333" });
    applyProps(materials.GreyElements, { metalness: 0, color: "#292929" });
    // Paint, from yellow to silver with paint chips
    applyProps(materials.WhiteCar, {
      roughness: 0.0,
      metalness: 0.15,
      color: "#202020",
      envMapIntensity: 2,
      normalMap: new THREE.CanvasTexture(
        new FlakesTexture(),
        THREE.UVMapping,
        THREE.RepeatWrapping,
        THREE.RepeatWrapping
      ),
      "normalMap-repeat": [40, 40],
      normalScale: [0.04, 0.04],
    });
  }, [nodes, materials]);
  return <primitive object={scene} {...props} />;
}
